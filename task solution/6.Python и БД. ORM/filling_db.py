import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sq
from create_db import create_tables, Publisher, Shop, Book, Stock, Sale
from configs import DSN, engine


create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('task solution/6.Python и БД. ORM/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()
