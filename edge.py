import cv2

k = cv2.imread('marie.jpg')
w,h = k.shape[:2]
k=cv2.resize(k,(int(h*0.5),int(w*0.5)))
# k = cv2.Canny(k,3,95)
k=cv2.GaussianBlur(k, (51,51),100)

cv2.imshow('Marie',k)
cv2.waitKey()
