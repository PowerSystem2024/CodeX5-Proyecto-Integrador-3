from conexion import get_db_connection

def registrar_usuario(nombre, apellido, correo, fecha_nacimiento, telefono, contraseña):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, correo, fecha_nacimiento, telefono, contraseña) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, apellido, correo, fecha_nacimiento, telefono, contraseña)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def iniciar_sesion(correo, contraseña):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nombre, rol FROM usuarios WHERE correo = %s AND contraseña = %s",
            (correo, contraseña)
        )
        usuario = cursor.fetchone()
        return usuario if usuario else None  # Devuelve (id, nombre, rol) o None
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None
    finally:
        cursor.close()
        conn.close()