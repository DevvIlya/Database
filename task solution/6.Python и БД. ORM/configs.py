import sqlalchemy

DSN = "postgresql+psycopg2://postgres:******@localhost:5432/netology_sqlalchemy"
engine = sqlalchemy.create_engine(DSN)