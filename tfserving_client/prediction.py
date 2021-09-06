from numpy.lib.type_check import imag
import tensorflow as tf
import numpy as np
import json
import requests
import cv2
from PIL import Image
import pprint
# from darkflow.net.build import TFNet

SERVER_URI='http://localhost:8501/v1/models/yolov4_test_model:predict'

class_list = {0:'person',1:'bicycle',2:'car',3:'motorbike',4:'aeroplane',5:'bus',6:'train',7:'truck',8:'boat',9:'traffic light',10:'fire hydrant',
                        11:'stop sign',12:'parking meter',13:'bench',14:'bird',15:'cat',16:'dog',17:'horse',18:'sheep',19:'cow',20:'elephant',
                        21:'bear',22:'zebra',23:'giraffe',24:'backpack',25:'umbrella',26:'handbag',27:'tie',28:'suitcase',29:'frisbee',30:'skis',
                        31:'snowboard',32:'sports ball',33:'kite',34:'baseball bat',35:'baseball glove',36:'skateboard',37:'surfboard',38:'tennis racket',39:'bottle',40:'wine glass',
                        41:'cup',42:'fork',43:'knife',44:'spoon',45:'bowl',46:'banana',47:'apple',48:'sandwich',49:'orange',50:'broccoli',
                        51:'carrot',52:'hot dog',53:'pizza',54:'donut',55:'cake',56:'chair',57:'sofa',58:'pottedplant',59:'bed',60:'diningtable',
                        61:'toilet',62:'tvmonitor',63:'laptop',64:'mouse',65:'remote',66:'keyboard',67:'cell phone',68:'microwave',69:'oven',70:'toaster',
                        71:'sink',72:'refrigerator',73:'book',74:'clock',75:'vase',76:'scissors',77:'teddy bear',78:'hair drier',79:'toothbrush' }


def preprocessing(image):
    image = image.resize((416, 416))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # print(image)
    return image


def predict(image):
    input_data = json.dumps(
        {
            "signature_name": "serving_default",
            "instances": image.tolist()
        }
    )

    response = requests.post(SERVER_URI, data = input_data.encode('utf-8'))
    json_response = json.loads(response.text)
    print(json_response)
    net_out = np.squeeze(np.array(json_response['predictions'], dtype='float32'))
    
#     detect_image = get_detect_result(net_out, image, 0.5, 0.4)


# def get_detect_result(output, img, conf_threshold, nms_threshold):
#     img_row = img.shape[1]
#     img_col = img.shape[2]
#     print(img_row, img_col)

#     draw_img = img.copy()
    
#     class_id_list = []
#     confidence_list = []
#     box_list = []

#     for idx, detection in enumerate(output):
#         score = detection[5:]
#         class_id = np.argmax(score)
#         confidence = score[class_id]

#         if confidence > conf_threshold :
#             center_x = int(detection[0] * img_col)
#             center_y = int(detection[1] * img_row)
#             width = int(detection[2] * img_col)
#             height = int(detection[3] * img_row)
#             left = int(center_x - width / 2)
#             top = int(center_y - height / 2)
#             print(class_id, confidence, center_x, center_y)

#             class_id_list.append(class_id)
#             confidence_list.append(float(confidence))
#             box_list.append([left, top, width, height])

#     nms_idx = cv2.dnn.NMSBoxes(box_list, confidence_list, conf_threshold, nms_threshold)

#     if len(nms_idx) >0 :
#         for i in nms_idx.flatten():
#             box = box_list[i]
#             left = box[0]
#             top = box[1]
#             width = box[2]
#             height = box[3]

#             caption = "{}: {:.4f}".format(class_list[class_id_list[i]], confidence_list[i])
#             print(caption)
#             cv2.rectangle(draw_img, (int(left), int(top)), (int(left+width), int(top+height)), (0,255,0), 1 ) 
#             cv2.putText(draw_img, caption, (int(left), int(top-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

#     return draw_img
