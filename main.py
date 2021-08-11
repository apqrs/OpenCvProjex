import cv2
import cv2 as cv
import mediapipe as mp
import imutils
import time

cap = cv.VideoCapture("videos/3.mp4")
ptime = 0
mPose = mp.solutions.pose
pose = mPose.Pose()
mpDraw = mp.solutions.drawing_utils
while 1:
    s, img = cap.read()
    imgRGB = cv.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)


    print(result.pose_landmarks)

    if result.pose_landmarks:
        print('#####')
        mpDraw.draw_landmarks(img, result.pose_landmarks, mPose.POSE_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv.putText(img,str(int(fps)), (100,300),cv2.FONT_ITALIC, 10, (0,255,0), 10)

    img = imutils.resize(img, height=720)
    cv.imshow("Video", img)
    cv.waitKey(1)
