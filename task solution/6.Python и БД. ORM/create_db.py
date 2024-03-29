from sqlalchemy import Table, Index, Integer, String, Column, Text, \
                       DateTime, Boolean, PrimaryKeyConstraint, \
                       UniqueConstraint, ForeignKeyConstraint, \
                        create_engine, MetaData, Table, Integer, \
                        String, Column, DateTime, ForeignKey, Numeric, func
import sqlalchemy as sq
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from configs import DSN, engine


Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)
    bk = relationship('Book', backref='publisher', uselist=False)

class Book(Base):
    __tablename__ = 'books'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    id_publisher = sq.Column(sq.Integer(), sq.ForeignKey('publisher.id'))
    stock = relationship("Stock")


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    count = sq.Column(sq.String(100), nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    shop = relationship("Shop")
    books = relationship("Book")

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.String(100), nullable=False)
    date_sale = sq.Column(sq.String(100), nullable=False)
    count = sq.Column(sq.String(100), nullable=False)
    id_stock = sq.Column(sq.Integer(), sq.ForeignKey('stock.id'))
    sl = relationship('Stock', backref='sale', uselist=False)

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)
    stock = relationship("Stock")

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# def create_tables(engine):
#     Base.metadata.create_all(engine)

def create_tables(engine):
    tabeles = (Publisher.__tablename__, 
                Book.__tablename__, 
                Stock.__tablename__, 
                Sale.__tablename__,
                Shop.__tablename__)
    for table_name in tabeles:
        if table_name in engine.table_names():
            return True
        else:
            Base.metadata.create_all(engine)
