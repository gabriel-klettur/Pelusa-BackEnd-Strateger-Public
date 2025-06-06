### 🧰 Comandos útiles de Git y tmux

| Acción                              | Comando                                       |
| ----------------------------------- | --------------------------------------------- |
| Ver estado de cambios               | `git status`                                  |
| Ver rama actual                     | `git branch`                                  |
| Cambiar de rama                     | `git checkout nombre_rama`                    |
| Crear nueva rama                    | `git checkout -b nombre_rama`                 |
| Ver ramas remotas                   | `git branch -r`                               |
| Agregar archivos al commit          | `git add archivo`                             |
| Agregar todos los archivos          | `git add .`                                   |
| Crear un commit                     | `git commit -m "mensaje"`                     |
| Hacer push                          | `git push origin nombre_rama`                 |
| Hacer pull                          | `git pull`                                    |
| Traer cambios remotos               | `git fetch`                                   |
| Ver diferencias antes de hacer pull | `git fetch && git diff origin/main`           |
| Ver diferencias local/remoto        | `git log HEAD..origin/main`                   |
| Ver log de commits                  | `git log --oneline`                           |
| Descartar cambios no staged         | `git restore archivo`                         |
| Descartar todos los cambios         | `git restore .`                               |
| Sincronizar con rebase              | `git pull --rebase origin main`               |
| Forzar push (con cuidado)           | `git push --force origin main`                |
| Guardar credenciales HTTPS          | `git config --global credential.helper store` |

---

### 🧰 Comandos útiles de tmux

| Acción                            | Comando                                         |
| --------------------------------- | ----------------------------------------------- |
| Ver sesiones activas              | `tmux ls`                                       |
| Crear nueva sesión                | `tmux new -s nombre`                            |
| Adjuntarse a sesión               | `tmux attach -t nombre`                         |
| Salir de sesión (dejar corriendo) | `Ctrl + B` luego `D`                            |
| Renombrar sesión                  | `Ctrl + B` luego `,`                            |
| Crear nueva ventana               | `Ctrl + B` luego `C`                            |
| Navegar ventanas                  | `Ctrl + B` luego `N` (siguiente)                |
| Cerrar ventana actual             | `exit`                                          |
| Matar sesión                      | `tmux kill-session -t nombre`                   |
| Crear nueva sesión desde tmux     | `Ctrl + B`, luego `:` y `new-session -s nombre` |

---

### 🧰 Comandos útiles de edición con `nano`

| Acción              | Comando                  |
| ------------------- | ------------------------ |
| Abrir archivo       | `nano archivo`           |
| Cortar línea actual | `Ctrl + K`               |
| Pegar línea         | `Ctrl + U`               |
| Guardar cambios     | `Ctrl + O` (luego Enter) |
| Salir de `nano`     | `Ctrl + X`               |

---

### 🌐 Comandos útiles de red de servidor

| Acción                                 | Comando                                                                           |
| -------------------------------------- | --------------------------------------------------------------------------------- |
| Ver IP pública                         | `curl ifconfig.me` o `curl ipinfo.io/ip`                                          |
| Ver IP interna                         | `ip a`                                                                            |
| Redirigir puerto 80 al 8001 (temporal) | `sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8001` |
| Hacer redirección persistente          | `sudo apt install iptables-persistent` y luego `sudo netfilter-persistent save`   |

---

### 🔐 Generar token de GitHub (HTTPS)

1. Ir a: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. "Generate new token" → classic o fine-grained
3. Asignar nombre, expiración y habilitar scope `repo`
4. Copiar token y usarlo en lugar de la contraseña en `git push`
5. (Opcional) Guardar token con:

   ```bash
   git config --global credential.helper store
   ```
