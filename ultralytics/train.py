import sys
# 现在就可以导入Yolo类了
from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO('/home/hutao/data1/FAN/YOLOv8-multi-task-PLCable-Colab/ultralytics/models/v8/PowerLine-MTYOLO.yaml', task='multi')  # .load('yolov8n.pt') # build a new model from YAML
    model = YOLO('/home/hutao/data1/FAN/YOLOv8-multi-task-PLCable-Colab/ultralytics/models/v8/PowerLine-MTYOLOv11.yaml',
                 task='multi')

    # model = YOLO("C:/Users/FRDISI/Desktop/[phD]yolov8_improve/YOLOv8-multi-task-PLCable/ultralytics/models/v8/yolov8-seg.yaml", task='multi')#.load('yolov8n.pt') # build a new model from YAML

    model.train(data='/home/hutao/data1/FAN/YOLOv8-multi-task-PLCable-Colab/ultralytics/datasets/bdd-multi-Cable.yaml',
                epochs=150,
                batch=32,
                imgsz=(640, 640),
                device=[0, 1],
                name='train',
                pretrained=False,
                rect=True,  # !-- Keep this line --!
                task='multi')
