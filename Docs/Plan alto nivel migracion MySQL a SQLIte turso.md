# Plan de alto nivel para la migración de MySQL a SQLIte en Turso

**Objetivo:** Migrar la base de datos de MySQL a SQLite hospedada en Turso, minimizando riesgos e interrupciones al servicio.

## Pasos

1. **Revisión de requisitos y análisis de compatibilidad** ✅ Completado
   - Inventario del esquema MySQL, volúmenes de datos y dependencias.
   - Detección de tipos y características de MySQL no soportadas por SQLite.
   - Dependencias confirmadas: FastAPI, SQLAlchemy, aiosqlite, SQLite3, Turso CLI.
   - Configuración actual en `config.py` usa MySQL (aiomysql) en desarrollo.
   - Modelos SQLAlchemy utilizan tipos compatibles con SQLite (INTEGER, TEXT, DATETIME, REAL).
   - No se detectaron características exclusivas de MySQL (procedimientos almacenados ni triggers complejos).
   - Directorio `data_sqlite` preparado para almacenamiento de archivos .sqlite.

2. **Diseño del esquema SQLite y scripts de transformación** ✅ Completado
   - Mapear tipos de datos y relaciones a estructuras compatibles con SQLite.
   - Elaborar scripts SQL para creación de tablas, índices y triggers.

3. **Exportación y transformación de datos desde MySQL** ✅ Completado
   - No hay datos previos; omitimos exportación y partimos de cero.

4. **Configuración de Turso y provisión de la base de datos SQLite** ✅ Completado
   - Variables de entorno `TURSO_AUTH_TOKEN` y `TURSO_DATABASE_URL` ya definidas en `.env`.
   - **Requisito previo:** habilitar Windows Subsystem for Linux (WSL):
     - https://learn.microsoft.com/en-us/windows/wsl/install
     - https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-1---enable-the-windows-subsystem-for-linux
     - https://www.reddit.com/r/bashonubuntuonwindows/comments/1by8mb3/wslregisterdistribution_failed_with_error/
   - Autenticación CLI: `turso login --token $Env:TURSO_AUTH_TOKEN`.
   - Crear instancias en Turso para cada base: alarms, estrategias, diary, positions, accounts, kline_data, orders.
   - Aprovisionar la instancia de SQLite en Turso.
   - Configurar accesos, backups automáticos y parámetros de rendimiento.

5. **Importación de datos a SQLite en Turso**
   - Ejecutar scripts de importación y carga masiva.
   - Verificar integridad referencial y completitud de datos.

6. **Pruebas finales, optimización y despliegue**
   - Realizar pruebas funcionales, de carga y rendimiento.
   - Ajustar índices y configuraciones de SQLite.
   - Definir plan de rollback y monitorización post-migración.
