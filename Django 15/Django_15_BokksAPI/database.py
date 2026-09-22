from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = (
    "mssql+pyodbc://admin:admin@localhost/BooksDb"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

Base = declarative_base()