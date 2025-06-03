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

2. **Diseño del esquema SQLite y scripts de transformación**
   - Mapear tipos de datos y relaciones a estructuras compatibles con SQLite.
   - Elaborar scripts SQL para creación de tablas, índices y triggers.

3. **Exportación y transformación de datos desde MySQL**
   - Generar dumps o exportar datasets a CSV.
   - Aplicar transformaciones necesarias (codificación, formatos de fecha, normalización).

4. **Configuración de Turso y provisión de la base de datos SQLite**
   - Aprovisionar la instancia de SQLite en Turso.
   - Configurar accesos, backups automáticos y parámetros de rendimiento.

5. **Importación de datos a SQLite en Turso**
   - Ejecutar scripts de importación y carga masiva.
   - Verificar integridad referencial y completitud de datos.

6. **Pruebas finales, optimización y despliegue**
   - Realizar pruebas funcionales, de carga y rendimiento.
   - Ajustar índices y configuraciones de SQLite.
   - Definir plan de rollback y monitorización post-migración.
