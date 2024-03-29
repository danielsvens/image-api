import os
import string
import random
import hashlib

from pathlib import Path
from image_service import app
from image_service.model.models import Image
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


class ImageService:

    def __init__(self):
        self.letters = string.ascii_letters + string.digits
        self.file_ending = None

    def validate_file(self, filename):
        split = filename.rsplit('.', 1)[1].lower()
        return filename != '' and '.' in filename and split in app.config['ALLOWED_EXTENSIONS']

    def image_handler(self, request, file):
        if not self.validate_file(file.filename):
            return 'error'

        self.file_ending = Path(file.filename).suffix
        #seed = self._generate_seed(file)
        filename = self.generate_filename(0)
        self.save_file(file, filename)
        url = self.build_url(filename, request.host_url)
        image_id = self.save_to_db(url, file, filename)

        return {'id': image_id, 'url': url}

    def generate_filename(self, seed: int):
        if seed != 0:
            random.seed(seed)
        filename = ''.join(random.choice(self.letters) for _ in range(40))

        return filename + self.file_ending

    @staticmethod
    def _generate_seed(file: FileStorage):
        h  = hashlib.sha256()
        buffer = 65536
        
        while n := file.stream.read(buffer):
            h.update(n)

        return int(h.hexdigest(), 32)

    @staticmethod
    def save_file(file, filename):
        file.save(os.path.join(app.config['STATIC_FOLDER'], filename))

    def save_to_db(self, url, file, filename):
        original_safe_name = secure_filename(file.filename)

        data = {
            'uri': url,
            'name': original_safe_name,
            'file_type': self.file_ending,
            'description': 'Image',
            'file_path': str(os.path.join(app.config['STATIC_FOLDER'], filename))
        }

        image = Image(data)
        return image.save_image()

    @staticmethod
    def build_url(filename, host):
        return f'{host}static/{filename}'
