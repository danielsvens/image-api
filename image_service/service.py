import os
import string
import random

from image_service import app
from image_service.models import Image 
from werkzeug.utils import secure_filename
from flask import url_for


class ImageService:

    def __init__(self):
        self.letters = string.ascii_letters + string.digits

    def validate_file(self, file):
        return file.filename != '' and self.allowed_file(file.filename)

    def image_handler(self, file):
        if not self.validate_file(file):
            return 'error'

        filename = self.generate_filename(file.filename)
        self.save_file(file, filename)
        image_id = self.save_to_db(file, filename)

        return {'id': image_id, 'url': self.build_url(filename)}

    def generate_filename(self, name):
        ending = os.path.splitext(name)[1].lower()
        filename = ''

        for _ in range(40):
            filename += random.choice(self.letters)

        return filename + ending

    def save_file(self, file, filename):
        file.save(os.path.join(app.config['STATIC_FOLDER'], filename))

    def save_to_db(self, file, filename):
        original_safe_name = secure_filename(file.filename)

        data = {
            'uri': filename,
            'name': original_safe_name,
            'file_type': os.path.splitext(filename)[1].lower(),
            'description': 'ProfilePicture',
            'file_path': str(os.path.join(app.config['STATIC_FOLDER'], filename))
        }

        image = Image(data)
        return image.save_image()

    def build_url(self, filename):
        return f'http://localhost:5000/v1/assets/image/{filename}'

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
