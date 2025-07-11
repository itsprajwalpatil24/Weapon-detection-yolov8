from ultralytics import YOLO

# Create a new YOLO model 
model = YOLO("yolov8n.yaml")  # You can also use 'yolov8s.yaml' or others based on your use case

# Start training 
model.train(
    data="path/to/data.yaml",   # ⚠️ Path to your dataset config file
    epochs=50,                  # Increase this for better results (try 100+ later)
    imgsz=640,                  # You can also try 416, 512, 720 depending on hardware
    batch=16,                   # Depends on your VRAM (reduce if OOM)
    name="weapon-first-train"  # This will create runs/detect/weapon-first-train
)
