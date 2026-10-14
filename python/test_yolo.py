from ultralytics import YOLO

# 加载YOLO模型（第一次运行它会自动下载一个6MB的小文件）
model = YOLO("yolov8n.pt")

# 识别一张网上的公交车图片
results = model("https://ultralytics.com/images/bus.jpg")

# 显示结果，并把识别后的图保存到本地
results[0].show()
results[0].save("result.jpg")
print("跑通了！结果保存在 result.jpg")