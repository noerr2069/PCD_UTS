import cv2

image = cv2.imread('C:\Users\Public\Pictures\Sample Pictures\Koala.jpg')
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('test_4.jpg', image)
