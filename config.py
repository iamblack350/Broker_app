import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_secret_key"

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or f"postgresql+psycopg2://username:password@localhost:5432/dbname"
    )
    SQLALCHEMY_TRACK_MODIFICATION = False

    DEBUG = True