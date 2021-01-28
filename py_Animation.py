import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc


width = 1280
height = 720
FPS = 24
seconds = 20
a = 250
paint_y = int(height/2)
fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./rectangulo.avi', fourcc, float(FPS), (width, height))
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

for paint_x in range(0, width+a, 6):
    frame = np.zeros((height, width,3),np.uint8)
    cv2.rectangle(frame,(paint_x, paint_y),(a,a),(0,0,255),-1)
    cv2.imshow('Animacion', frame)
    cv2.putText(frame,"Rectangulo",(150,100),font,1,(0,0,255),2,cv2.LINE_AA)
    video.write(frame)

video.release()
 