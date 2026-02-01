#!/usr/bin/env python3
import cv2

print("Testing all camera devices...")
for i in range(10):
    try:
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"✅ Device {i} works! Frame shape: {frame.shape}")
            else:
                print(f"⚠️  Device {i} opened but can't read")
            cap.release()
    except Exception as e:
        print(f"❌ Device {i} error: {e}")
