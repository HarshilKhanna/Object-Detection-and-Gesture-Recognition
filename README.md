# Object Detection and Gesture Recognition

This project uses **MediaPipe** and **OpenCV** to perform real-time **gesture recognition** using a webcam. It detects hand landmarks and identifies the number of fingers held up or whether the hand is forming a **fist, palm, or individual finger gesture**.

## Features

- **Real-time hand tracking** using MediaPipe.
- Detects the number of fingers raised (up to 5 fingers).
- Identifies basic hand gestures like:
  - **Palm** (all fingers up)
  - **Fist** (no fingers up)
  - **Single Finger Up** (identifies which finger is up).
- Displays real-time **FPS (Frames Per Second)** for performance monitoring.

## Technologies Used

- **Python**  
- **OpenCV** (for video capture and display)  
- **MediaPipe** (for hand tracking and landmark detection)

## Installation

1. Clone the repository:
```bash
https://github.com/your-username/gesture-recognition.git
```

2. Navigate to the project directory:
```bash
cd gesture-recognition
```

3. Install the required libraries:
```bash
pip install opencv-python mediapipe
```

## How It Works

- The webcam captures the video stream.
- MediaPipe detects hand landmarks.
- The program analyzes the relative position of finger landmarks to determine:
  - If a particular finger is up or down.
  - Whether the hand is forming a palm, fist, or raising one finger.
- The FPS is also calculated and displayed in real-time.

## Usage

Run the Python script:
```bash
python gesture_recognition.py
```

### Controls
- **Show Palm:** All fingers up - displays "Palm".
- **Make a Fist:** No fingers up - displays "Fist".
- **Show One Finger:** Raises one finger - displays the name of the raised finger.
- Press **'q'** to exit the application.

## Expected Output
- Real-time video feed with hand tracking.
- On-screen text showing:
  - The number of fingers up.
  - The gesture (Palm, Fist, or the name of the raised finger).
- FPS value to monitor performance.

## Future Enhancements
- Add support for more complex hand gestures.
- Integrate with smart home devices for control via hand gestures.
- Use deep learning models for more accurate gesture recognition.

---

Enjoy recognizing gestures with your webcam! 🚀

