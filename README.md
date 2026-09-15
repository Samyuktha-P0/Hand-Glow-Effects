# Magic Hand Glow Effect

A real-time computer vision application that uses MediaPipe and OpenCV to detect hand landmarks and generate an interactive glow trail effect based on fingertip movement. The project demonstrates real-time hand tracking, image processing, and visual effect generation using Python.

## Overview

This application captures live video from a webcam, detects hand landmarks using MediaPipe Hands, and tracks the index fingertip. As the fingertip moves, a glowing trail is rendered and blended with the camera feed to create an interactive visual effect.

## Features

* Real-time webcam processing
* Hand landmark detection using MediaPipe
* Index fingertip tracking
* Dynamic glow trail rendering
* Smooth visual effects using Gaussian blur
* Lightweight implementation with minimal dependencies

## Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe**
* **NumPy**

## Installation

### Clone the Repository

```bash
git clone https://github.com/Samyuktha-P0/Hand-Glow-Effects.git
cd Hand-Glow-Effects
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install opencv-python mediapipe numpy
```

## Usage

Run the application:

```bash
python hand_effect.py
```

The webcam window will open automatically. Move your hand in front of the camera to generate the glow effect.

### Controls

| Key | Description          |
| --- | -------------------- |
| ESC | Exit the application |

## Project Workflow

1. Capture frames from the webcam.
2. Process frames using MediaPipe Hands.
3. Detect and track the index fingertip landmark.
4. Render a trail based on fingertip movement.
5. Apply Gaussian blur to create a glow effect.
6. Blend the glow layer with the original frame.
7. Display the processed output in real time.

## Project Structure

```text
Hand-Glow-Effects/
│
├── hand_effect.py
├── requirements.txt
└── README.md
```

## Applications

* Computer Vision Learning
* Human–Computer Interaction
* Interactive Art Installations
* Gesture-Based Interfaces
* Real-Time Visual Effects

## Future Enhancements

* Multi-color glow modes
* Gesture-based effect switching
* Particle and sparkle systems
* Multi-hand interaction
* Recording and export functionality
* Customizable visual themes

## Author

**Samyuktha**

GitHub: https://github.com/Samyuktha-P0

## License

This project is available for educational and personal use.
