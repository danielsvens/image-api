from image_service import db
from datetime import datetime
from marshmallow import fields, Schema


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(255))
    file_type = db.Column(db.String(255))
    name = db.Column(db.String(255))
    description = db.Column(db.Text())
    file_path = db.Column(db.String(255))
    added_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, data):
        self.id = data.get('id')
        self.uri = data.get('uri')
        self.file_type = data.get('file_type')
        self.name = data.get('name')
        self.description = data.get('description')
        self.file_path = data.get('file_path')

    def save_image(self):
        assert self.id is None, 'Id must be None'

        db.session.add(self)
        db.session.commit()

        return self.id

    @classmethod
    def get_image(cls, image_id):
        return cls.query.get(image_id) if isinstance(image_id, int) else None

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.id}>'


class ImageSchema(Schema):
    id = fields.Int(dump_only=True)
    uri = fields.String(dump_only=True)
    name = fields.String(dump_only=True)
    file_type = fields.String(dump_only=True)
    description = fields.String(dump_only=True)
    file_path = fields.String(dump_only=True)
    added_date = fields.DateTime(dump_only=True)
