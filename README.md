### RetinaNet Custom data 학습
#### Github 주소 - https://github.com/fizyr/keras-retinanet
#### RetinaNet 학습 블로그 주소
[`https://blog.naver.com/ee1210/222445460599`](https://blog.naver.com/ee1210/222445460599)
#### RetinaNet 학습 오류 해결 블로그 주소
[`https://blog.naver.com/ee1210/222447266757`](https://blog.naver.com/ee1210/222447266757)
<!-- #### [RetinaNet 학습 오류 해결 블로그 주소](https://blog.naver.com/ee1210/222447266757) -->

  ---
### YOLOv5 Custom data 학습
#### Github 주소 - https://github.com/ultralytics/yolov5
- `git clone https://github.com/ultralytics/yolov5`
- 폴더 구조
```bash
├── data
│   ├── images
│   │   ├── train
│   │   │   └── .jpg ...
│   │   ├── valid
│   │   │   └── .jpg ...
│   ├── labels 
│   │   ├── train
│   │   │   └── .txt ...
│   │   │   valid
│   └── └── └── .txt ...
│
├── image_train.txt
├── image_valid.txt
│
└── yolov5
``` 
- labels/ ~.txt 내용 예시 (annotation)
  - class_index x(center) y(center) width height
  - `12 0.214609053497942 0.437037037037037 0.395473251028807 0.398765432098765`
- image_train.txt 내용 예시 (train 이미지 경로 모음 )
  - `/content/drive/MyDrive/YOLOv5/data/images/train/B290101XX_01194.jpg`
- yolov5 전처리 코드
  - [code](https://github.com/deeplearningTeamSeven/DeepLearning/blob/main/YOLOv5/yolo_preprocessing.ipynb)

 --- 
### YOLOv4 Custom data 학습 - 최종 선택 모델
#### Github 주소 - https://github.com/AlexeyAB/darknet
- `git clone https://github.com/AlexeyAB/darknet`
- 폴더 구조
```bash
├── annotation
│   ├── train
│   │   ├── .jpg ...
│   │   ├── .txt ...
│   ├── valid
│   │   ├── .jpg ...
│   └── └── .txt ...
├── train.txt 
├── valid.txt 
├── yolov4-custom.cfg
├── obj.data
├── obj.names
├── training
└── darknet
``` 
- yolov4 전처리 코드
  - [code](https://github.com/deeplearningTeamSeven/DeepLearning/blob/main/YOLOv4/yolo_preprocessing.ipynb)
  
