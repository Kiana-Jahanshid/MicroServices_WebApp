from flask import Flask , request , jsonify , send_file
import numpy as np
from PIL import Image
from image_classification import YOLOv8
import io 
import base64
import cv2

app = Flask(__name__)
detector = YOLOv8("models/yolov8n.onnx")

@app.route("/" , methods=["GET"])
def root():
    return {"HELLO" : "world"}


@app.route("/objectdetection" , methods=["POST"])
def object_detection():
    image = request.files["file"]
    image = Image.open(image.stream)
    img_np_array = np.array(image)
    img , labels = detector(img_np_array)
    result = {"labels":labels}

    # Encode the image (or mat object) in a format that can be included in the JSON, such as base64 encoding.
    # Return the image as a separate request (via a URL) or as part of the JSON response.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    pil_img = Image.fromarray(img_rgb)
    img_io = io.BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)

    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    json_response = {
        'image': img_base64  , # base64 image string
        'labels': result
    }

    return jsonify(json_response)



# flask run