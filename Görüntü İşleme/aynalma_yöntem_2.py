import cv2

img = cv2.imread('araba.png')
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
cv2.imshow('orgin', img)

img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('cv_rotate_90_clockwise.jpg', img_rotate_90_clockwise)
# True

img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('cv_rotate_90_counterclockwise.jpg', img_rotate_90_counterclockwise)
# True

img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('data/dst/lena_cv_rotate_180.jpg', img_rotate_180)
# True



cv2.waitKey()
cv2.destroyAllWindows()