# SentinelEye - Drowsiness Detection System

A real-time drowsiness detection web application that uses computer vision to monitor eye aspect ratio (EAR) and alert users when drowsiness is detected. Built with MediaPipe Tasks Vision, Node.js, and Python.

## Features

- **Real-time Eye Tracking**: Uses MediaPipe Face Landmarker for accurate facial landmark detection
- **Eye Aspect Ratio (EAR) Calculation**: Monitors both eyes to detect drowsiness patterns
- **Visual Feedback**: Live diagnostics with EAR values, system latency, and status indicators
- **Alert System**: Visual and textual alerts when drowsiness is detected
- **Web-based Interface**: Runs entirely in the browser with webcam access
- **Raspberry Pi Integration**: Streams video from Pi camera to web interface
- **REST API**: Backend endpoint for logging drowsiness events

## Prerequisites

- Node.js (v14 or higher)
- Python 3.7+
- OpenCV (for Pi camera streaming)
- A modern web browser with webcam support
- Internet connection (for loading MediaPipe models)
- Raspberry Pi with camera (optional, for remote streaming)

## Installation

1. Clone the repository:
```bash
git clone <your-github-repo-url>
cd drowsiness-detector
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface Only (Local Webcam)

1. Start the server:
```bash
npm start
```

2. Open your browser and navigate to `http://localhost:3000`

3. Click "Activate Sensor" to enable webcam access

4. The system will begin monitoring your eye aspect ratio in real-time

### With Raspberry Pi Camera

1. On the Raspberry Pi, run the camera streamer:
```bash
python3 main.py
```

2. On the server machine, start the Node.js server:
```bash
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

4. The video feed from the Pi will be displayed and monitored

## How It Works

The system uses the Eye Aspect Ratio (EAR) method to detect drowsiness:

- **EAR Calculation**: Measures the ratio of eye height to eye width using facial landmarks
- **Threshold Detection**: Triggers alerts when EAR falls below 0.22 for more than 1.5 seconds
- **Real-time Processing**: Processes video frames at high frequency for immediate response

## API Endpoints

### POST /api/log-event
Logs drowsiness detection events to the console.

**Request Body:**
```json
{
  "timestamp": "2024-01-29T10:00:00.000Z",
  "type": "drowsiness_detected",
  "earValue": 0.18
}
```

## Configuration

- **EAR_THRESHOLD**: 0.22 (configurable in `index.html`)
- **DROWSY_TIME**: 1500ms (1.5 seconds of continuous low EAR before alert)
- **Port**: 3000 (or set `PORT` environment variable)
- **Pi Camera Device**: `/dev/video4` (configurable in `main.py`)

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

Requires webcam permissions and WebGL support for MediaPipe processing.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This system is for demonstration purposes and should not be used as a substitute for professional driver monitoring systems in real-world applications. Always prioritize safety and never rely solely on automated systems.