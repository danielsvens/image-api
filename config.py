import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
TESTING = False
SECRET_KEY = os.environ.get('SECRET')
DB_URI = f'postgresql://{os.environ.get("PGUSER")}:{os.environ.get("PGPASSWORD")}@{os.environ.get("PGPORT")}:{os.environ.get("DB_PORT")}/{os.environ.get("PGDATABASE")}'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'production'
PORT = 80

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
STATIC_FOLDER = os.path.join('/var/www', 'static/')
