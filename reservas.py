from conexion import get_db_connection


def verificar_disponibilidad(fecha, hora, cancha):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM reservas WHERE fecha = %s AND hora = %s AND cancha = %s",
            (fecha, hora, cancha),
        )
        reserva = cursor.fetchone()
        return reserva is None  # True si está disponible, False si ya está reservado
    except Exception as e:
        print(f"Error al verificar disponibilidad: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


def crear_reserva(usuario_id, fecha, hora, cancha):
    if not verificar_disponibilidad(fecha, hora, cancha):
        return False
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reservas (usuario_id, fecha, hora, cancha) VALUES (%s, %s, %s, %s)",
            (usuario_id, fecha, hora, cancha),
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al crear reserva: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


def ver_reservas(usuario_id):
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, fecha, hora, cancha FROM reservas WHERE usuario_id = %s",
            (usuario_id,),
        )
        reservas = cursor.fetchall()
        return reservas
    except Exception as e:
        print(f"Error al ver reservas: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def ver_todas_reservas():
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT r.id, r.usuario_id, u.nombre, r.fecha, r.hora, r.cancha FROM reservas r JOIN usuarios u ON r.usuario_id = u.id"
        )
        reservas = cursor.fetchall()
        return reservas
    except Exception as e:
        print(f"Error al ver todas las reservas: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def eliminar_reserva(reserva_id):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservas WHERE id = %s", (reserva_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error al eliminar reserva: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
