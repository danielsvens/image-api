import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from edMQ_client.client import ProducerClient

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from image_service.model.models import Image
db.create_all()

from image_service.rest import routes

producer = ProducerClient(app.config['EDMQ_URL'], app.config['SECRET'])
producer.start()
