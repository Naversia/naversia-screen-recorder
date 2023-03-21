# naversia-screen-recorder
This Python script captures the screen and computer camera in real-time and saves the resulting video as an MP4 file. Here's how to use the script:

Requirements:

    Python 3.x
    OpenCV
    PIL
    NumPy

Installation:

    Install Python 3.x on your computer.
    Install the necessary libraries by running the following commands in the command prompt:
        pip install opencv-python
        pip install Pillow
        pip install numpy

Usage:

    Run the script in a Python environment.
    The script will automatically start recording the screen and the computer camera.
    To stop the recording, press the 'q' key.
    The resulting video file will be saved in the same directory as the script, with a timestamp as its filename.

Note:

    The script captures the entire screen by default. You can change the dimensions of the captured area by modifying the 'bbox' parameter in the 'ImageGrab.grab()' function.
    The script captures the first available computer camera by default. If you have multiple cameras connected, you can modify the '0' parameter in the 'cv2.VideoCapture()' function to select a different camera.
    The script captures the computer camera in addition to the screen. If you don't want to capture the camera, you can comment out the relevant lines in the script.
    The script captures video at 20 frames per second by default. You can modify this value by changing the 'fps' variable.
    The resulting video file may be large, depending on the length of the recording. Make sure you have enough storage space before running the script.
