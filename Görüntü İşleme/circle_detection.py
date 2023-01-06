import cv2
import numpy as np

img = cv2.imread("circles.jpg")
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.blur(imgGRAY,(3,3))
#3e 3 matrixlerle tarama yaparak eşit bir şekilde blurlama işlemi yapıyor.

gauss= cv2.GaussianBlur(imgGRAY,(9,9),sigmaX=7)
#gauss blur da orta kesende kanarlara doğru bir bulanıklaştırma işlemi yapar.

imgCanny = cv2.Canny(imgBlurred,80,80)
#imgBlurred ya da Canny üzerinde denenebilir, maskeleme




circles = cv2.HoughCircles(imgBlurred, cv2.HOUGH_GRADIENT, 1, 20,
                            minRadius=2, maxRadius=130,
                            param1=50, param2=30)
#(_,_,1,20) farklı dairler arası mesafe

print(circles)
#(kaynak,moted,)
circles = np.uint16(np.around(circles))   #integer'a çevir, noktalrın değerinin anlamak için 


for circle in circles:
    for x,y,r in circle:
        cv2.circle(img, (x,y), r, [0,0,255], 2)
        cv2.circle(img, (x,y), 2, [0,0,0], 2)
#circle içindeki liste gir liste içindeki xyr değerinlerinin içinde gez.
cv2.imshow("img",imgCanny)

cv2.waitKey()
cv2.destroyAllWindows()