import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTING = True
#SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@database:5432/image_service'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgresUser:postgrePassword@192.168.1.8:5432/image_service'
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'development'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
STATIC_FOLDER = os.path.join(BASE_DIR, "staticfiles")

## EDMQ CONFIG

EDMQ_URL = 'edmq://guest:guest@localhost:5672'
EXCHANGE_NAME = 'e.default'
