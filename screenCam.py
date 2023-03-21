import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

#we callimg them with 0 and 1 to the correct width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
fps = 20.0
timeStamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{timeStamp}.mp4'
# print(timeStamp)
#4 caractors for doing codding and incoding our file
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#we will pass info' first file name, the second incoding encoding, third the frame size, four width and height 
captured_video = cv2.VideoWriter(file_name, fourcc, fps, (width, height))

computerCam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    #convert the image into array of images
    img_np = np.array(img)
    #make the RGB coloe semilar to the screen
    img_last = cv2.cvtColor(img_np, cv2.COLOR_BGRA2RGB)
    #read the computer camera
    _, frame = computerCam.read()

    frameHeight, frameWidth, _ = frame.shape
    # print(frameHeight, frameWidth)
    #mix the pic one on the other two dimention array
    #we take the posiioin on the left side and position it on the right side
    img_last[0:frameHeight, 0:frameWidth, :] = frame[0: frameHeight, 0:frameWidth, :]
    #we call cv2 to show the images
    cv2.imshow('Secret Capture', img_last)
    #show the computer camera
    # cv2.imshow('computerCam', frame)
    captured_video.write(img_last)
    #when the user pressing 'q' its stopping
    if cv2.waitKey(10) == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()