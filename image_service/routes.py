from flask import jsonify, request, make_response, send_from_directory
from image_service import app
from image_service.models import ImageSchema, Image
from image_service.service import ImageService


image_schema = ImageSchema()
img_service = ImageService()


@app.route('/v1/image/upload', methods=['POST'])
def upload_image():

    if 'file' not in request.files:
        return make_response('image not found', 404)

    file = request.files['file']
    response = img_service.image_handler(file)

    return make_response(jsonify(response), 200)


@app.route('/v1/image/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = Image.get_image(image_id)

    if image is None:
        return make_response('image not found', 404)

    serialized = image_schema.dump(image)
    return make_response(jsonify(serialized), 200)


@app.route('/v1/assets/image/<path:filename>', methods=['GET'])
def get_image_info(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)
