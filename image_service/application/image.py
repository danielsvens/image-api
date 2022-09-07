import os
import string
import random
import hashlib

from image_service import app
from image_service.model.models import Image
from werkzeug.utils import secure_filename


class ImageService:

    def __init__(self):
        self.letters = string.ascii_letters + string.digits

    def validate_file(self, file):
        return file.filename != '' and self.allowed_file(file.filename)

    def image_handler(self, request, file):
        if not self.validate_file(file):
            return 'error'

        seed = self._generate_seed(file)
        filename = self.generate_filename(file.filename, seed)
        self.save_file(file, filename)
        url = self.build_url(filename, request.host_url)
        image_id = self.save_to_db(url, file, filename)

        return {'id': image_id, 'url': url}

    def generate_filename(self, name, seed: int):
        ending = os.path.splitext(name)[1].lower()
        random.seed(seed)
        filename = ''.join(random.choice(self.letters) for _ in range(40))

        return filename + ending

    @staticmethod
    def _generate_seed(filename):
        h  = hashlib.sha256()
        b  = bytearray(128 * 1024)
        mv = memoryview(b)
        
        with open(filename, 'rb', buffering=0) as f:
            while n := f.readinto(mv):
                h.update(mv[:n])

        return int(h.hexdigest(), 32)

    @staticmethod
    def save_file(file, filename):
        file.save(os.path.join(app.config['STATIC_FOLDER'], filename))

    @staticmethod
    def save_to_db(url, file, filename):
        original_safe_name = secure_filename(file.filename)

        data = {
            'uri': url,
            'name': original_safe_name,
            'file_type': os.path.splitext(filename)[1].lower().replace('.', ''),
            'description': 'Image',
            'file_path': str(os.path.join(app.config['STATIC_FOLDER'], filename))
        }

        image = Image(data)
        return image.save_image()

    @staticmethod
    def build_url(filename, host):
        return f'{host}static/{filename}'

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
