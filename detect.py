print("Program started")
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


results = model("test.jpg", save=True)

print("Detection completed!")