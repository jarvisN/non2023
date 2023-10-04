import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # โหลดโมเดล YOLOv5 small
img = 'image/eagle.jpg'  # ตัวอย่าง path ของรูปภาพ
results = model(img)
results.show()  # แสดงผลลัพธ์
