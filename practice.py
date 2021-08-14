import cv2

image = cv2.imread("small.jpg")
h, w = image.shape[:2]
image = cv2.resize(image, (int(w * 0.5), int(0.5 * h)))

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 150, 255, cv2.THRESH_BINARY)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# draw contours on the original image
image_copy = image.copy()
# cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=1,
#                  lineType=cv2.LINE_AA)

for i, contour in enumerate(contours[5:6]):  # loop over one contour area
    for j, contour_point in enumerate(contour):  # loop over the points
        # draw a circle on the current contour coordinate
        cv2.circle(image_copy, (contour_point[0][0], contour_point[0][1]), 2, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Marie", image_copy)
cv2.waitKey()
