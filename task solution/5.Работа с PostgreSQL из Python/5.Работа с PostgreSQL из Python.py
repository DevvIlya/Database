import psycopg2


conn = psycopg2.connect(database="netology_db", 
                        user="postgres", 
                        password="6857+Asd", 
                        host="localhost", 
                        port=5432)
with conn.cursor() as cur:
    cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY);")
    conn.commit()
conn.close()


        def create_db(conn):
            pass

        def add_client(conn, first_name, last_name, email, phones=None):
            pass

        def add_phone(conn, client_id, phone):
            pass

        def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
            pass

        def delete_phone(conn, client_id, phone):
            pass

        def delete_client(conn, client_id):
            pass

        def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
            pass


        with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
            pass  # вызывайте функции здесь

        conn.close()
