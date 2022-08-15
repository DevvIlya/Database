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

q = session.query(Publisher).filter(Publisher.id == input("Введите идентификатор (id) издателя "))
for s in q.all():
    print(s.id, s.name)

print('======>')

subq = session.query(Shop).all()
for s in subq:
    print(s.id, s.name)

session.commit()