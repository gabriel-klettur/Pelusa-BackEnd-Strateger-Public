**Guía para obtener un certificado SSL en EC2 Ubuntu**

---

## 1. Resumen de la situación actual

**Servidor / Instancia EC2 (Ubuntu)**

* **IP pública**: `13.53.91.100`
* En el servidor Ubuntu, la aplicación backend corre en el puerto `8001`.
* Actualmente, el puerto `80` está redirigido internamente hacia el `8001` para recibir datos de TradingView.

**Dominio y DNS (GoDaddy)**

* **Dominio principal**: `www.gabriel-klettur.com`
* **Subdominio API**: `api.gabriel-klettur.com` (A record apuntando a `13.53.91.100`)
* Registros DNS configurados en GoDaddy:

  ```
  Type  | Name | Data           | TTL
  ─────────────────────────────────────────
  A     | @    | 76.76.21.21    | 600 seconds   ← (para frontend en Vercel)
  A     | api  | 13.53.91.100   | 1 Hour        ← (para backend en EC2)
  NS    | @    | ns15.domaincontrol.com. | 1 Hour
  ```

  * Con esto, `api.gabriel-klettur.com` resuelve hacia la instancia EC2.

**Frontend y Base de Datos**

* Frontend desplegado en Vercel sobre `gabriel-klettur.com`.
* Base de datos en Neon.
* El frontend consumirá la API mediante `https://api.gabriel-klettur.com` (incluyendo WebSockets seguros `wss://`).

**Objetivo del SSL**

* Obtener un certificado Let’s Encrypt para `api.gabriel-klettur.com`.
* Asegurar HTTPS y WSS sin advertencias de seguridad.
* No es posible usar solo la IP para emitir el certificado; debe usarse el nombre de dominio.

---

## 2. Resultado de Let’s Debug para validación HTTP-01

**Test result for api.alexis-klettur.com using http-01**

```
ANotWorking
Error
api.alexis-klettur.com has an A (IPv4) record (13.53.91.100) but a request to this address over port 80 did not succeed. Your web server must have at least one working IPv4 or IPv6 address.
Get "http://api.alexis-klettur.com/.well-known/acme-challenge/letsdebug-test": dial tcp 13.53.91.100:80: connect: connection refused

Trace:
@0ms: Making a request to http://api.alexis-klettur.com/.well-known/acme-challenge/letsdebug-test (using initial IP 13.53.91.100)
@0ms: Dialing 13.53.91.100
@9ms: Experienced error: dial tcp 13.53.91.100:80: connect: connection refused

IssueFromLetsEncrypt
Error
A test authorization for api.alexis-klettur.com to the Let's Encrypt staging service has revealed issues that may prevent any certificate for this domain being issued.
13.53.91.100: Fetching http://api.alexis-klettur.com/.well-known/acme-challenge/xw4CJ0ooNBWoxm2O50OLhxrL_ibsPzmI8uvBB6DD0F8: Connection refused
Submitted 6s ago. Sat in queue for 1ms. Completed in 4s. Show verbose information.

We also have open-source API and CLI tools, as well as web-based certificate search and certificate revocation.

Let's Encrypt™ is a trademark of the Internet Security Research Group (ISRG).

Let's Debug is not affiliated with, or sponsored or endorsed by, ISRG.
```

> **Interpretación**: El servidor no responde en el puerto 80, por lo que Let’s Encrypt no puede verificar el token. Esto se debe a que actualmente todo el tráfico HTTP se está redirigiendo al puerto 8001 y no hay ningún servicio escuchando en 80.

---

## 3. Desafíos y estrategias para HTTP-01 Challenge

Para que Let’s Encrypt pueda verificar la propiedad del dominio mediante HTTP-01, debe poder acceder a:

```
http://api.gabriel-klettur.com/.well-known/acme-challenge/<token>
```

en el puerto TCP 80. Sin embargo, nuestra app actualmente no escucha directamente en el 80.

### Opciones disponibles:

1. **Modo standalone de Certbot (temporariamente usar puerto 80)**

   * Detener o deshabilitar la redirección 80→8001 durante el proceso de validación.
   * Certbot levanta su servidor temporal en el 80 para responder al challenge.
   * Una vez validado, reiniciar la app/redirect.

2. **Modo webroot con nginx (o similar)**

   * Instalar y configurar nginx para que escuche en el puerto 80.
   * Evitar que nginx reenvíe todo tráfico a 8001. Solo enrutar “/.well-known/acme-challenge/” a un directorio específico (ej. `/var/www/html/`).
   * Para el resto, nginx hace proxy\_pass a `localhost:8001`.
   * Luego, Certbot usaría `--webroot -w /var/www/html` para colocar los archivos de validación.
   * Después de emitir, nginx también se configura para servir HTTPS (443) y reenviar tráfico a 8001.

3. **DNS-01 Challenge (API GoDaddy)**

   * Usar plugin DNS de Certbot para GoDaddy: requiere API key y secret de GoDaddy.
   * Crear un record TXT `_acme-challenge.api.gabriel-klettur.com` con el valor del challenge.
   * Más complejo de automatizar inicialmente, pero no requiere exponer puerto 80.

**Recomendación inicial**: Empezar con **opción 2 (webroot + nginx)**:

* Configuración más estándar, permite tener nginx como proxy inverso permanente.
* Evita parar servicios (TradingView) en producción.

---

## 4. Pasos recomendados (estrategia Webroot + nginx)

### Paso 4.1: Instalar nginx y Certbot

```bash
sudo apt update
sudo apt install -y nginx
sudo ufw allow 'Nginx Full'   # Abre puertos 80 y 443 en firewall local
sudo apt install -y certbot python3-certbot-nginx
```

Verifica que nginx está funcionando:

```bash
sudo systemctl start nginx
overify=$(curl -I http://127.0.0.1)
echo "$verify"
```

Debe devolver un encabezado HTTP con `200 OK`.

### Paso 4.2: Configurar nginx para el subdominio “api.gabriel-klettur.com” (HTTP)

Crear un nuevo bloque de servidor en `/etc/nginx/sites-available/api.gabriel-klettur.com` con el contenido:

```nginx
server {
    listen 80;
    server_name api.gabriel-klettur.com;

    # Ruta para los challenges de Let's Encrypt
    root /var/www/html;

    location ~ /.well-known/acme-challenge/ {
        allow all;
        try_files $uri =404;
    }

    # Proxy para el resto del tráfico HTTP hacia la app en 8001
    location / {
        proxy_pass http://localhost:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Luego:

```bash
sudo ln -s /etc/nginx/sites-available/api.gabriel-klettur.com /etc/nginx/sites-enabled/
sudo nginx -t    # Verifica sintaxis
sudo systemctl reload nginx
```

Con esto, nginx atenderá en el puerto 80:

* Las peticiones a `/.well-known/acme-challenge/` las servirá desde `/var/www/html/.well-known/acme-challenge/`.
* Resto de peticiones (API) las reenviará a `localhost:8001`.

### Paso 4.3: Probar ruta del challenge localmente

```bash
sudo mkdir -p /var/www/html/.well-known/acme-challenge/
echo "test-content" | sudo tee /var/www/html/.well-known/acme-challenge/test-file
curl http://api.gabriel-klettur.com/.well-known/acme-challenge/test-file
```

Debería devolverte “test-content”. Si no, revisar puertos abiertos en EC2 Security Group (ver sección 7).

### Paso 4.4: Ejecutar Certbot con webroot

```bash
sudo certbot certonly --webroot -w /var/www/html -d api.gabriel-klettur.com
```

* Certbot colocará archivos de validación en `/var/www/html/.well-known/acme-challenge/`.
* Si todo va bien, terminará emitiendo el certificado y lo guardará en `/etc/letsencrypt/live/api.gabriel-klettur.com/`.

### Paso 4.5: Configurar nginx para HTTPS

Editar `/etc/nginx/sites-available/api.gabriel-klettur.com`, agregando un bloque para 443:

```nginx
server {
    listen 443 ssl;
    server_name api.gabriel-klettur.com;

    ssl_certificate /etc/letsencrypt/live/api.gabriel-klettur.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.gabriel-klettur.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://localhost:8001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

# Redirigir HTTP a HTTPS
server {
    listen 80;
    server_name api.gabriel-klettur.com;
    return 301 https://$host$request_uri;
}
```

Luego:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Verifica:

```
curl -I https://api.gabriel-klettur.com
```

Debe devolver `200 OK` con certificado válido.

### Paso 4.6: Probar WebSocket seguro (WSS)

En tu frontend, haz una conexión a:

```
wss://api.gabriel-klettur.com/ws-endpoint
```

Si tu backend usa WebSocket en la misma ruta proxy, debería funcionar sin errores de certificación.

### Paso 4.7: Renovación automática del certificado

Certbot instala automáticamente un cron job o systemd timer para renovar. Puedes probar:

```bash
sudo certbot renew --dry-run
```

Si no hay errores, la renovación está automatizada.

---

## 5. Datos a verificar en cada iteración

* **IP y puerto**:

  * IP pública: `13.53.91.100`.
  * App backend en `localhost:8001`.
  * nginx escuchando en `80` y `443`.
* **DNS**:

  * `api.gabriel-klettur.com` → 13.53.91.100.
  * TTL bajo para pruebas (recomendado: 1h o menos).
* **Firewall (Security Group)**: Verificar reglas que permitan:

  * Puerto 80 TCP (0.0.0.0/0)
  * Puerto 443 TCP (0.0.0.0/0)
  * Puerto 8001 (solo si necesitas acceso directo desde internet; si es solo proxy, no hace falta abrir 8001 a 0.0.0.0)
* **Pruebas**:

  1. `curl http://api.gabriel-klettur.com/.well-known/acme-challenge/test-file`
  2. `sudo certbot certonly --webroot …`
  3. `curl -I https://api.gabriel-klettur.com`
  4. Conexión WSS desde el frontend.

---

## 6. Prompt resumen (recuerda usarlo íntegro en cada consulta)

> Actúa como un experto en certificados SSL en Ubuntu (EC2) y en configuración de Amazon EC2. Te proporciono mi infraestructura y requisitos para que me indiques paso a paso cómo obtener e instalar un certificado Let’s Encrypt para mi subdominio:
>
> 1. **Servidor / Instancia EC2 (Ubuntu)**
>
>    * IP pública: 13.53.91.100
>    * La app backend corre en el puerto 8001.
>    * El puerto 80 redirige internamente al 8001 (datos de TradingView).
> 2. **Dominio y DNS configurados en GoDaddy**
>
>    * Dominio principal: `www.gabriel-klettur.com`
>    * Subdominio API: `api.gabriel-klettur.com` → 13.53.91.100 (A record).
>    * Registros DNS actuales en GoDaddy:
>
>      ```
>      Type  | Name | Data           | TTL             
>      ───────────────────────────────────────────────
>      A     | @    | 76.76.21.21    | 600 seconds     
>      A     | api  | 13.53.91.100   | 1 Hour          
>      NS    | @    | ns15.domaincontrol.com. | 1 Hour
>      ```
> 3. **Requisitos específicos**
>
>    * El certificado debe cubrir HTTPS (+ WSS) sin advertencias.
>    * Frontend en Vercel consumirá la API vía `https://api.gabriel-klettur.com`.
>    * Actualmente no hay servicio escuchando en el 80 (redirección a 8001).
>    * Usar Let’s Encrypt (Certbot) para generar e instalar el certificado.
> 4. **Consideraciones de despliegue**
>
>    * Explica la estrategia recomendada (standalone vs. webroot vs. DNS).
>    * Comandos de instalación de Certbot (snap o apt).
>    * Para standalone: cómo detener la redirección 80→8001 temporalmente.
>    * Para webroot: cómo configurar nginx para servir `/.well-known/acme-challenge` y proxy\_pass hacia 8001.
>    * Configuración final de nginx para HTTPS 443 y proxy a 8001.
>    * Comprobaciones finales (`curl`, wss).
> 5. **Datos importantes a reiterar**
>
>    * IP: `13.53.91.100`
>    * Dominio: `api.gabriel-klettur.com`
>    * Puerto interno de la app: `8001`
>    * Puertos abiertos en Security Group: 80, 443, (8001 si es necesario).
>
> **Este prompt servirá como esquema base para cada consulta hasta lograr el certificado SSL.**
> Cada vez que me indiques un paso, te enviaré resultados de comandos y logs. Actualiza el prompt si algo cambia.
>
> **Objetivo final**: Certificado Let’s Encrypt en `/etc/letsencrypt/live/api.gabriel-klettur.com/` y renovación automática.

---

## 7. Configuración de Security Group en AWS (reglas actuales)

A continuación se muestran las reglas de entrada (Inbound) configuradas en el Security Group de la instancia EC2 (captura adjunta):

| Type       | Protocol | Port range | Source           | Descripción              |
| ---------- | -------- | ---------- | ---------------- | ------------------------ |
| Custom TCP | TCP      | 8000       | 0.0.0.0/0        | OPEN DOOR                |
| Custom TCP | TCP      | 8000       | 34.174.168.65/32 | Siteground – Pelusa Tra… |
| HTTP       | TCP      | 80         | 0.0.0.0/0        | OPEN DOOR 3              |
| HTTPS      | TCP      | 443        | 0.0.0.0/0        | OPEN DOOR 2              |
| HTTP       | TCP      | 80         | 157.97.6.174/32  | Iceland Home – DEV – A…  |
| RDP        | TCP      | 3389       | 157.97.6.174/32  | Iceland Home RDP         |
| Custom TCP | TCP      | 8000       | 157.97.6.174/32  | Iceland Home – DEV – P…  |
| HTTP       | TCP      | 80         | 34.212.75.30/32  | TradingView IP 2 – ALA…  |
| HTTP       | TCP      | 80         | 52.32.178.7/32   | TradingView IP 4 – ALA…  |
| HTTP       | TCP      | 80         | 52.89.214.238/32 | TradingView IP 1 – ALA…  |
| SSH        | TCP      | 22         | 157.97.6.174/32  | Iceland Home SSH         |
| HTTP       | TCP      | 80         | 54.218.53.128/32 | TradingView IP 3 – ALA…  |

**Notas sobre Security Group**:

* Ya existe una regla para HTTP (puerto 80) abierta a 0.0.0.0/0 (ID: sgr-0836747fb1d863cb8). Esto permite que Let’s Encrypt pueda conectarse al puerto 80.
* Existe también la regla de HTTPS (puerto 443) abierta a 0.0.0.0/0 (ID: sgr-0101a332a224f0210).
* El puerto `8001` (en el que corre la app) no aparece explícitamente: actualmente se exponen puertos `8000` con varias fuentes, pero no hay ningún ‘Custom TCP’ para `8001`. Si se desea acceder a `8001` directamente desde internet, habría que agregarlo. Sin embargo, **no es necesario** si nginx va a hacer proxy\_pass internamente.

---

> Con todo esto listo, estamos preparados para seguir cada paso y solucionar el problema de la validación HTTP-01 y la instalación del certificado.

---

**Fin de la Guía – documento listo para usarse como referencia**
