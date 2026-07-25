from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    if "users" in inspector.get_table_names():
        columns = {column["name"] for column in inspector.get_columns("users")}
        with engine.begin() as connection:
            if "experience_level" not in columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN experience_level VARCHAR"))
            if "name" not in columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN name VARCHAR"))
            if "role" not in columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN role VARCHAR"))
            if "password" not in columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN password VARCHAR"))
