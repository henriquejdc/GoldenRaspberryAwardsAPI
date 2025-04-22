import os

from sqlalchemy import create_engine, orm

ENV = os.getenv("ENV", "dev")
DATABASE_PATH = "test.db" if ENV == "test" else "database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{DATABASE_PATH}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = orm.declarative_base()

def reset_db():
    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)

def init_db():
    from . import models  # Import models to register them with SQLAlchemy
    reset_db()
    Base.metadata.create_all(bind=engine)
