import sys
# 现在就可以导入Yolo类了
from ultralytics import YOLO

if __name__ == '__main__':

    number = 2 #input how many tasks in your work
    model = YOLO("/content/PowerLine-MTYOLO-NANO-150Epochs.pt")  # Validate the model
    model.predict(source='/content/MulticableData/MulticableData/images/val2017', imgsz=(640,640), device=[0],name='FTMAPS', augment=False,save=True,task='multi', conf=0.25, iou=0.45,  show_labels=True)
