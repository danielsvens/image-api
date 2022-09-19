import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
TESTING = False
SECRET_KEY = os.environ["SECRET"]
SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'production'
PORT = 8082

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
STATIC_FOLDER = os.path.join('/var/www', 'static/')
