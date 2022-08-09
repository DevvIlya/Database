import psycopg2


# удалить таблицы
# def delete_tables(conn):

#     cur.execute('''
#     drop table phones;
#     drop table users;
#     ''')

#1 создать таблицу
def create_tables(conn):

    cur.execute("""
    create table if not exists users(
    id serial primary key,
    name varchar(60),
    surname varchar(60),
    email varchar(80) unique);
    
    create table if not exists phones(
    id serial primary key,
    users_id int references users(id) on delete cascade,
    phone varchar(12));
    """)
    conn.commit()

#2 добавить нового клиента
def add_user(conn,name,surname,email,phone=None):

    cur.execute("""
    insert into users(name,surname,email)
    values(%s,%s,%s) returning id;
    """,(name,surname,email))
    users_id = cur.fetchone()
    print(f'{users_id=}')
    cur.execute("""
    insert into phones(users_id,phone)
    values(%s,%s);
    """, (users_id,phone))
    conn.commit()

#3 добавить телефон
def add_phone(conn, name,surname,email,phone):

    cur.execute("""
    select id from users
    where (name,surname,email)=(%s,%s,%s);
    """, (name, surname, email))
    users_id = cur.fetchone()
    print(f'{users_id=}')
    cur.execute("""
    insert into phones(users_id,phone)
    values(%s,%s);
    """, (users_id, phone))
    conn.commit()

#4 изменить данные о клиенте
def update_info(conn, id, name,surname,email,phone):

    cur.execute("""
        update users 
        set 
        name = %s,
        surname = %s,
        email = %s
        where id = %s;
        """, (name, surname, email,id))

    cur.execute("""
        update phones
        set phone = %s
        where users_id = %s;
        """, (phone,id))
    conn.commit()

#5 удалить телефон
def delete_phone(conn, id, phone):

    cur.execute("""
        delete from phones
        where users_id = %s and phone = %s
        """, (id, phone))
    conn.commit()

#6 удалить клиента
def delete_user(conn, id):

    cur.execute("""
            delete from users
            where id = %s 
            """, (id,))
    conn.commit()

#7 найти клиента
def find_user(conn, name=None, surname=None, email=None, phone=None):

    if phone is None:
        cur.execute("""
            select name, surname, email, phone from users
            join phones on users.id = phones.users_id
            where name = %s or surname = %s or email = %s;
            """, (name, surname, email))
        info = cur.fetchall()
        print(f'{info=}')

    else:
        cur.execute("""
        select users_id from phones
        where phone = %s;""", (phone,))
        users_id = cur.fetchone()

        cur.execute("""
                    select name, surname, email, phone from users
                    join phones on users.id = phones.users_id
                    where users.id = %s;""", (users_id,))
        info = cur.fetchall()
        print(f'{info=}')





with psycopg2.connect(database='netology_db',
                        user='postgres',
                        password='',
                        host='localhost',
                        port='5432') as conn:
    with conn.cursor() as cur:
        # delete_tables(conn)
        create_tables(conn)
        add_user(conn, 'Roman', 'Abasov', 'Abasov@gmail.com')
        add_user(conn,'Anton','Bubnov','buben@gmail.com','+79219999999')
        add_phone(conn,'Anton','Bubnov','buben@gmail.com','+71111111111')
        add_user(conn,'Alina','Malina','malina@gmail.com','+78888888888')
        add_user(conn, 'Andrey', 'Baranov', 'Baranov@gmail.com', '+71212121212')
        update_info(conn, 1, 'Greg','Kozzlov','Kozzlov@gmail.com','22222222')
        find_user(conn, name='Anton',phone = '+71111111111')