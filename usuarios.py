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