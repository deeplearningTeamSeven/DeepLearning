from flask_inference import image_preprocessing, load_model
from flask import Flask, request
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        print('사진', file)
        print('사진이름', file.filename)

        if file.filename == '':
            response_object = {
                'status': 'Bad Request',
                'message': 'No Selected File'
            }
            return response_object, 400
        else :
            image = request.files['image'].read()
            image = cv2.imdecode(np.fromstring(image, dtype = np.uint8), cv2.IMREAD_COLOR)
            print(image)

            origin_image, input = image_preprocessing(image, (512, 512))
            load_model(origin_image, input)
    
    return '<h1>Hello Flask!</h1>'

if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=8000, debug=True)
    



