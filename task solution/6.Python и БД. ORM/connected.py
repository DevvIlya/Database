import sqlalchemy

DSN = "postgresql+psycopg2://postgres:6857+Asd@localhost:5432/netology_sqlalchemy"
engine = sqlalchemy.create_engine(DSN)