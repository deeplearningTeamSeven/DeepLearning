import io
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import resize
from prediction import predict, preprocessing #원래이거임
# from prediction2 import predict 
# from prediction import preprocessing
from PIL import Image
from flask import Flask, render_template, url_for, request, redirect
from requests.models import Response
import tensorflow as tf
import os
# import model
import numpy as np
import json
import requests
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
            image = Image.open(io.BytesIO(image))
            image = preprocessing(image)
            predict(image)
    
    return '<h1>Hello Flask!</h1>'

if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port=8000, debug=True)
    



