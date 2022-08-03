import psycopg2


#1 создать таблицу
def create_db(conn):
    
    cur.execute("""
    create table if not exists users(
    id serial primary key,
    first_name varchar(60),
    last_name varchar(60),
    email varchar(60) unique);
        
    create table if not exists phones(
    id serial primary key,
    users_id int references users(id on delete cascade,
    phone varchar(12));
    """)
    conn.commit()

#2 добавить нового клиента
def add_client(conn, first_name, last_name, email, phones=None):
    cur.execute("""
    insert into users(first_name,last_name,email)
    values(%s,%s,%s) returning id;
    """,(first_name,last_name,email))
    users_id = cur.fetchone()
    print(f'{users_id=}')
    cur.execute("""
    insert into phones(users_id,phones)
    values(%s,%s);
    """, (users_id,phones))
    conn.commit()

#3 добавить телефон
def add_phone(conn, first_name,last_name,email,phones):
    cur.execute("""
    select id from users
    where (first_name,last_name,email)=(%s,%s,%s);
    """, (first_name, last_name, email))
    users_id = cur.fetchone()
    print(f'{users_id=}')
    cur.execute("""
    insert into phone(users_id,phones)
    values(%s,%s);
    """, (users_id, phones))
    conn.commit()

#4 изменить данные о клиенте
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    cur.execute("""
        update users 
        set 
        name = %s,
        surname = %s,
        email = %s
        where id = %s;
        """, (first_name, last_name, email,client_id))

    cur.execute("""
        update phones
        set phone = %s
        where users_id = %s;
        """, (phones,client_id))
    conn.commit()

#5 удалить телефон
def delete_phone(conn, id, phones):

    cur.execute("""
        delete from phones
        where users_id = %s and phone = %s
        """, (id, phones))
    conn.commit()

#6 удалить клиента
def delete_user(conn, id):

    cur.execute("""
            delete from users
            where id = %s 
            """, (id,))
    conn.commit()

#7 найти клиента
def find_user(conn, first_name=None, last_name=None, email=None, phones=None):

    if phones is None:
        
        cur.execute("""
            select first_name, last_name, email, phones from users
            join phones on users.id = phones.users_id
            where first_name = %s or last_name = %s or email = %s;
            """, (first_name, last_name, email))
        info = cur.fetchall()
        print(f'{info=}')

    else:
        print('Find user with phone!')
        cur.execute("""
        select users_id from phones
        where phone = %s;""", (phones,))
        users_id = cur.fetchone()

        cur.execute("""
                    select first_name, last_name, email, phone from users
                    join phones on users.id = phones.users_id
                    where users.id = %s;""", (users_id,))
        info = cur.fetchall()
        print(f'{info=}')