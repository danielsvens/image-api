import config
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from image_service.models import Image
db.create_all()

from image_service import routes
