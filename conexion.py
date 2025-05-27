# conexion.py
import psycopg2

def get_db_connection():
    try:
        conexion = psycopg2.connect(
            dbname="ProyectoIntegrador",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

# Para probar la conexión (directamente desde este archivo)
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        tablas = cursor.fetchall()
        print("Tablas en la base:", tablas)
        cursor.close()
        conn.close()
        print("Conexión exitosa!")