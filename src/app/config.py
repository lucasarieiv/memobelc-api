from dotenv import load_dotenv
from os import path, environ

# basedir = path.abspath(path.join(path.dirname(__file__), "../../"))
# load_dotenv(path.join(basedir, ".env"))


class Config:
    PYTHONPATH = "src"
    MONGO_URI = environ.get("MONGO_URI")
    SECRET_KEY = environ.get("SECRET_KEY")
    STRIPE_SECRET_KEY = environ.get("STRIPE_SECRET_KEY")
    PRICE_ID = environ.get('PRICE_ID')
    STRIPE_WHSEC = environ.get("STRIPE_WHSEC")
    GENAI_API_KEY = environ.get("GENAI_API_KEY")
    GENAI_MODEL = environ.get("GENAI_MODEL")

    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = environ.get("MAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")
    
    FRONT_BASE_URL = environ.get("FRONT_BASE_URL")

    FLASK_ENV = "development"
    PORT = int(environ.get("PORT"))



