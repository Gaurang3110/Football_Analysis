from ultralytics import YOLO

# model = YOLO("yolov8m.pt")  #predict1
model = YOLO("models/best.pt")   #predict2 - roboflow custom trained model

results = model.predict("input_videos/08fd33_4.mp4",save=True)
print(results[0])

for box in results[0].boxes:
  print('***********************')
  print(box)
