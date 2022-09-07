import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTING = False
# SECRET = '50a6e8403cd6f392'
SECRET = 'Super le secret '
#SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@database:5432/image_service'
SQLALCHEMY_DATABASE_URI = f'postgresql://postgresUser:postgresPassword@192.168.1.4:32014/image'
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'production'
PORT = 8082

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
STATIC_FOLDER = os.path.join('/var/www', 'static/')

## EDMQ CONFIG
EDMQ_URL = 'edmq://guest:guest@192.168.1.4:32021'
