# Face Detection Attendance System

A Python application that uses facial recognition to mark attendance in real-time. The system captures faces from a webcam, compares them with stored images, and records attendance in a CSV file.

## Features

- Real-time face detection and recognition.
- Automatic attendance marking based on recognized faces.
- Easy addition of new faces by placing images in the `ImagesAttendance` directory.

## Requirements

- Python 3.8 or higher
- OpenCV
- face_recognition
- numpy

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Aaryan33/Face-Detection-Attendance-System.git
   ```
2. Install the required packages:
   ```
   pip install opencv-python face_recognition numpy
   ```     

## Run

1. **Ensure your webcam is connected.**

2. **Start the attendance tracking:**
   Open your terminal, navigate to the project directory, and run:
   ```bash
   python attendance_project.py
   ```
