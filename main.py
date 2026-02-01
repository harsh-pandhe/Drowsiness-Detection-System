import cv2
import socketio
import base64
import time
import sys

# Configuration - HD 4MP WEBCAM
DEVICE = "/dev/video4"  # SHENZHEN Fullhan HD 4MP WEBCAM (correct device!)
DEVICE_ALT = "/dev/video5"  # Alternative device path for HD 4MP WEBCAM
SERVER = "http://localhost:3000"
FPS = 15

# Connect to server
print("🔌 Connecting to server...")
try:
    sio = socketio.Client()
    sio.connect(SERVER, wait_timeout=10)
    print("✅ Connected to server")
except Exception as e:
    print(f"❌ Failed to connect to server: {e}")
    print("💡 Make sure the server is running: npm start")
    sys.exit(1)

# Open HD 4MP WEBCAM
print(f"📷 Opening HD 4MP WEBCAM...")

# Try multiple approaches to open the camera
camera_opened = False

# Approach 1: Try device path with V4L2
print(f"   Trying {DEVICE} with V4L2...")
cap = cv2.VideoCapture(DEVICE, cv2.CAP_V4L2)
if cap.isOpened():
    camera_opened = True
    print(f"   ✅ {DEVICE} opened!")

# Approach 2: Try alternative device path
if not camera_opened and DEVICE_ALT:
    print(f"   Trying {DEVICE_ALT} with V4L2...")
    cap = cv2.VideoCapture(DEVICE_ALT, cv2.CAP_V4L2)
    if cap.isOpened():
        camera_opened = True
        print(f"   ✅ {DEVICE_ALT} opened!")

# Approach 3: Try device indices (device 4 might work as index)
if not camera_opened:
    for idx in [4, 5]:
        print(f"   Trying device index {idx}...")
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            camera_opened = True
            print(f"   ✅ Device {idx} opened!")
            break

if not camera_opened:
    print(f"❌ Cannot open HD 4MP WEBCAM")
    print("💡 The HD 4MP WEBCAM appears to be incompatible with OpenCV on this system.")
    print("   This camera may require specialized drivers or software.")
    print("   Using fallback ASUS FHD webcam instead...")
    
    # Fallback to ASUS FHD webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ No working camera found!")
        sys.exit(1)
    print("✅ Using ASUS FHD webcam (device 0)")

# Try to set camera properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, FPS)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# Get actual camera properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
actual_fps = int(cap.get(cv2.CAP_PROP_FPS))

print(f"✅ Camera opened: {width}x{height} @ {actual_fps} FPS")
print("📊 Dashboard: http://localhost:3000")
print("⏸️  Press Ctrl+C to stop\n")

frame_count = 0
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to read frame, retrying...")
            time.sleep(0.1)
            continue

        # Encode frame to JPEG
        _, jpg = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
        b64 = base64.b64encode(jpg).decode("utf-8")

        # Send frame to server
        sio.emit("pi_frame", b64)
        
        frame_count += 1
        if frame_count % (FPS * 10) == 0:  # Every 10 seconds
            print(f"📸 Streamed {frame_count} frames")
        
        time.sleep(1 / FPS)

except KeyboardInterrupt:
    print("\n\n⏹️  Stopping stream...")
finally:
    cap.release()
    sio.disconnect()
    print("✅ Cleanup complete")
