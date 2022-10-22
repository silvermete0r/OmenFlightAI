import cv2
import time
#importing the necessary libraries

birds_cascade = cv2.CascadeClassifier('models/birds-cascade.xml')
#definition of haar cascades for bird recognition
 
cap = cv2.VideoCapture('testing/video.mp4')
#getting a video

pTime = 0
birds_max = 0
#variables for fps output

#video frame processing cycle for bird recognition 
while True: 
 
    ret, img = cap.read() 
    #img = cv2.imread("test_images/bird.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detecting birds in the frame
    birds = birds_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5, maxSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

    #selection of birds in the frame
    for(x, y, w, h) in birds:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,255),2)
        cv2.putText(img, 'Detected Bird', (x, y - 10 if y > 20 else y + 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,255), 2)

    #getting the value of frames per second
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #getting the value of number of birds per frame
    if(len(birds)>birds_max):
        birds_max=len(birds)

    #output the value of FPS and Number of birds per frame
    cv2.putText(img, "FPS: " + str(int(fps)), (30,70), cv2.FONT_HERSHEY_PLAIN, 2.5, (100,100,0), 3, cv2.FILLED)
    cv2.putText(img, f"Birds Detected: {birds_max}", (30,120), cv2.FONT_HERSHEY_PLAIN, 2.5, (100,100,0), 3, cv2.FILLED)

    #show the window of the received video data
    cv2.imshow('OmenFlight Detected Birds', img)
 
    #pressing "ESC" will stop the program
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
#termination of video processing and closing of windows
cap.release()
cv2.destroyAllWindows() 