import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv()

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(basedir, "database.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
