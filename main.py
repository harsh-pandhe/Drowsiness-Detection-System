import cv2
import socketio
import base64
import time

DEVICE = "/dev/video4"
SERVER = "http://localhost:3000"
FPS = 15

sio = socketio.Client()
sio.connect(SERVER)

cap = cv2.VideoCapture(DEVICE, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    raise RuntimeError("❌ Cannot open HD 4MP WEBCAM")

print("✅ Streaming from", DEVICE)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    _, jpg = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
    b64 = base64.b64encode(jpg).decode("utf-8")

    sio.emit("pi_frame", b64)
    time.sleep(1 / FPS)
