# Sistema de Reservas - Grupo CodeX5

Este proyecto es un sistema de reservas de canchas deportivas con una ventana fácil de usar (no es por consola) y guarda los datos en una base de datos PostgreSQL.

---

## Guía fácil: ¿Cómo hago para que funcione en mi PC?

### 1. Descarga el proyecto
- Descarga el repositorio desde GitHub o copia todos los archivos a una carpeta nueva en tu computadora.

### 2. Instala Python
- Si no tienes Python, descárgalo e instálalo desde [python.org](https://www.python.org/downloads/).
- Asegúrate de elegir la versión 3.10 o superior.

### 3. Instala PostgreSQL
- Descarga e instala PostgreSQL desde [postgresql.org](https://www.postgresql.org/download/).
- Recuerda el usuario y la contraseña que elijas durante la instalación.

### 4. Crea un entorno virtual (opcional, recomendado)
- Abre PowerShell en la carpeta del proyecto y ejecuta:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- Si ves (venv) al principio de la línea, el entorno está activo.
- **IMPORTANTE:** Si descargaste el proyecto y ves una carpeta `venv`, bórrala antes de crear la tuya. Nunca copies la carpeta `venv` de otra PC.

### 5. Instala las dependencias (los programas que necesita Python)
- Ejecuta este comando en la misma ventana:
  ```powershell
  pip install -r requirements.txt
  ```
- Si te da error, prueba con:
  ```powershell
  pip install customtkinter psycopg2-binary tkcalendar pillow requests
  ```
- **NOTA:** No intentes instalar `tkinter` por pip, ya viene con Python.

### 6. Crea la base de datos en PostgreSQL
- Abre el programa pgAdmin (o DBeaver, o la terminal de PostgreSQL).
- Ejecuta este comando (puedes copiar y pegar):
  ```sql
  CREATE DATABASE nombre_base;
  ```
- Cambia `nombre_base` por el nombre que quieras (por ejemplo: reservas_canchas).

### 7. Configura la conexión a la base de datos en el archivo conexion.py

- Abre el archivo `conexion.py` con un editor de texto (por ejemplo, VS Code o Bloc de notas).
- Busca la parte donde se define la conexión, que debería verse así:
  ```python
  import psycopg2

  def get_connection():
      return psycopg2.connect(
          dbname="nombre_base",
          user="usuario",
          password="contraseña",
          host="localhost",
          port="5432"
      )
  ```
- Cambia los valores por los de tu base de datos. Por ejemplo, si tu base se llama `ProyectoIntegrador`, tu usuario es `postgres` y tu contraseña es `admin`, déjalo así:
  ```python
  def get_connection():
      return psycopg2.connect(
          dbname="ProyectoIntegrador",
          user="postgres",
          password="admin",
          host="localhost",
          port="5432"
      )
  ```
- Guarda el archivo.

Así, el sistema sabrá cómo conectarse a tu base de datos cada vez que lo uses.

### 8. Crea las tablas automáticamente
- Ejecuta:
  ```powershell
  python init_db.py
  ```
- Si todo está bien, verás: `Base de datos y tablas creadas correctamente.`

### 9. Abre el sistema de reservas
- Ejecuta:
  ```powershell
  python interfaz.py
  ```
- Se abrirá una ventana para usar el sistema.

### 10. ¡Listo para usar!
- Haz clic en "Registrarse" para crear tu usuario.
- Inicia sesión y prueba crear, ver o cancelar reservas.
- Si tienes un usuario admin, prueba el panel de administrador.

---

## ¿Qué hago si algo no funciona?
- Si ves un error como "Fatal error in launcher...", borra la carpeta `venv` y vuelve a crear el entorno virtual desde cero.
- Revisa que los datos de usuario, contraseña y base de datos estén bien escritos.
- Asegúrate de que PostgreSQL esté abierto y funcionando.

---

## ¿Cómo está organizado el proyecto?
```
ProyectoIntegrador/
├── interfaz.py         # Ventana principal del sistema
├── usuarios.py         # Todo lo de usuarios (registrar, login)
├── reservas.py         # Todo lo de reservas (crear, ver, eliminar)
├── conexion.py         # Conexión a la base de datos
├── init_db.py          # Script para crear las tablas automáticamente
├── requirements.txt    # Lista de programas que necesita Python
```

---
¡Siguiendo estos pasos, cualquier persona puede instalar y usar el sistema en su PC, aunque no sepa de programación!

