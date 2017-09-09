import cv2

image = cv2.imread('C:\Users\Public\Pictures\Sample Pictures\Koala.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.namedWindow("TestWindow", cv2.WINDOW_AUTOSIZE)
cv2.imwrite('test_2.jpg', gray)

