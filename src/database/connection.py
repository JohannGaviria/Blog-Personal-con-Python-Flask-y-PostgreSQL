from decouple import config
import psycopg2
import traceback

def connectionDB():
    try:
        conn = psycopg2.connect(
            host=config('POSTHOST'),
            database=config('POSTDB'),
            user=config('POSTUSER'),
            password=config('POSTPASS')
        )

        if conn is not None:
            print("Conexión exitosa a la base de datos.")
            return conn
    except Exception as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        traceback.print_exc()
        return None
