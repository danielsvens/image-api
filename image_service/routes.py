from flask import jsonify, request, make_response
from image_service import app
from image_service.models import ImageSchema, Image
from image_service.service import ImageService


image_schema = ImageSchema()
img_service = ImageService()


@app.route('/v1/image/upload', methods=['POST'])
def upload_image():

    if 'image' not in request.files:
        return make_response('image not found in request', 400)

    file = request.files['image']
    response = img_service.image_handler(file)

    return make_response(jsonify(response), 200)


@app.route('/v1/image/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = Image.get_image(image_id)

    if image is None:
        return make_response('image not found', 404)

    serialized = image_schema.dump(image)
    return make_response(jsonify(serialized), 200)
