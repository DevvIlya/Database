import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import sessionmaker, relationship
from sqlalchemy import func
from pprint import pprint
import sqlalchemy as sq
from sqlalchemy.orm.util import join
from sqlalchemy.sql.selectable import subquery
from configs import DSN, engine
from filling_db import Publisher, Shop, Book, Stock, Sale
from create_db import create_tables


Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

q = session.query(Publisher).filter(Publisher.name == input("Введите название издателя "))
for s in q.all():
    print(s.id, s.name)

print('=========================>')

q = session.query(Publisher).filter(Publisher.id == input("Введите идентификатор (id) издателя "))
for s in q.all():
    print(s.id, s.name)

print('=========================>')

# запрос выборки магазинов, продающих книги издателя
def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')

if __name__ == '__main__':
    searching_publisher_id()

session.commit()