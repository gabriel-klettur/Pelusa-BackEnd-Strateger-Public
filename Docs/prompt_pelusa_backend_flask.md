# Rol: Actua como un experto en desarrollo de software

Actua como un experto en Python.

## Descripcion del Proyecto: Pelusa BackEnd

### Resumen del Proyecto:
El proyecto es una plataforma backend diseñada para automatizar el proceso de trading basado en señales (alarmas) recibidas desde TradingView. Las funcionalidades clave incluyen la recepción de alarmas, procesamiento y ejecución de operaciones en el exchange BingX, almacenamiento y gestión de datos de operaciones, y obtención de datos de velas. La aplicación está construida para ser escalable, segura y fácil de mantener, aprovechando tecnologías modernas como FastAPI para la creación de APIs y SQLAlchemy para la gestión de bases de datos.

### Funcionalidades Pricipales:

1. **Recepción de Alarmas de TradingView**
    - Endpoint: /webhook
    - Descripción: Recibe alarmas de TradingView en formato JSON a través de un webhook. Valida y guarda las alarmas en la base de datos 'Desarrollo-Alarmas'.

2. **Gestión de Alarmas**
    - Guardar Alarmas: Las alarmas recibidas se almacenan en la base de datos con detalles como el ticker, temporalidad, cantidad, precios de entrada y salida, 
    hora de la alarma, orden y estrategia.
    - Consultar Alarmas: Provee endpoints para consultar las alarmas almacenadas, con opciones de paginación y filtrado por las más recientes.

3. **Procesamiento de Alarmas para Operaciones**
    - Descripción: Procesa las alarmas para determinar si se deben ejecutar operaciones de compra o venta en BingX, basado en las estrategias configuradas. Realiza 
    estas operaciones a través de la API de BingX.

4. **Gestión de Estrategias**
    - Crear Estrategias: Permite la creación de estrategias de trading que definen cuándo y cómo se deben realizar las operaciones basadas en las alarmas recibidas.
    - Actualizar Estrategias: Permite la actualización de estrategias existentes.
    - Consultar Estrategias: Provee endpoints para consultar y listar estrategias existentes.
    - Eliminar Estrategias: Permite la eliminación de estrategias no deseadas.

5. **Gestión de Operaciones**
    - Guardar Operaciones: Almacena información de las operaciones realizadas en la base de datos 'Desarrollo-Operaciones', incluyendo detalles como el tipo de operación, 
    cantidad, precio, y timestamp.
    - Consultar Operaciones: Provee endpoints para consultar las operaciones almacenadas.
    
6. **Obtención de Datos de Velas**
    - Descripción: Solicita información de las velas a la API de BingX y guarda esta información en la base de datos 'Desarrollo-Velas'.
    - Endpoint: /get-k-line-data
    - Parámetros: Permite obtener datos de velas para un símbolo específico, intervalo, límite, y rango de fechas.

7. **Gestión de Balance y Posiciones**
    - Consultar Balance: Endpoints para consultar el balance en diferentes tipos de cuentas (Spot, Perpetual USDT-M, Perpetual COIN-M).
    - Consultar Posiciones: Endpoint para obtener las posiciones actuales del usuario.

8. **Logging y Monitoreo**
    - Logging: Uso de Loguru para mantener registros detallados de las operaciones, alarmas recibidas, y cualquier error ocurrido.
    - Monitoreo del Servidor: Middleware para registrar solicitudes inválidas, IPs no autorizadas, y estado del servidor.
9. Seguridad
    - Filtrado de IPs: Middleware para permitir o bloquear solicitudes basadas en la IP del cliente.
    - Manejo de Excepciones: Gestión centralizada de excepciones para asegurar respuestas consistentes y registrar errores.

### Tecnologias Utilizadas:
- Python
- MYSQL (Database)
- SQAlchemy (ORM para SQL en Python)
- FastAPI (Construccion de APIs)
- Loguru (Logging compatible con FastAPI)
- Uvicorn (Servidor ASGI rápido y ligero) Utilizado para desarrollo
- Gunicorn (Servidor WSGI escalable y robusto) Utilizado para produccion
- aiomysql (Driver async para MySQL)

### Estructura de Directorios Actual:
(((
Mi estructura de directorios actual es:
'''


'''
)))

## Solicitudes de Implementación:
Te pediré que me ayudes a mejorar e implementar ideas en mi código cuando lo necesite. Esperarás mis instrucciones para proceder.


