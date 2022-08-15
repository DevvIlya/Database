from sqlalchemy import Table, Index, Integer, String, Column, Text, \
                       DateTime, Boolean, PrimaryKeyConstraint, \
                       UniqueConstraint, ForeignKeyConstraint, \
                        create_engine, MetaData, Table, Integer, \
                        String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from connected import DSN, engine

# engine = create_engine("postgresql+psycopg2://postgres:6857+Asd@localhost:5432/netology_sqlalchemy")

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    bk = relationship('Book', backref='publisher', uselist=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    id_publisher = Column(Integer(), ForeignKey('publisher.id'))
    stock = relationship("Stock")


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    count = Column(String(100), nullable=False)
    id_book = Column(Integer, ForeignKey('books.id'))
    id_shop = Column(Integer, ForeignKey('shop.id'))
    shop = relationship("Shop")
    books = relationship("Book")

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(String(100), nullable=False)
    date_sale = Column(String(100), nullable=False)
    count = Column(String(100), nullable=False)
    id_stock = Column(Integer(), ForeignKey('stock.id'))
    sl = relationship('Stock', backref='sale', uselist=False)

class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    stock = relationship("Stock")

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

def create_tables(engine):
    Base.metadata.create_all(engine)
