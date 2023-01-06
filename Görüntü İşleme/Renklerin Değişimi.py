import cv2
import numpy as np

resim = cv2.imread("resim.png")

#resim[:,:, 0] = 255

#cv2.imshow("Blue Degeri Maximum",resim)
"""
resim[:,:, 2] = 255 
cv2.imshow("Red Degeri Maximum",resim)
#resim[:,:, 1] = 255   green değeri max
#resim[:,:, 2] = 255   red değeri max
"""

#3 kanallı ama ben sadece kırmızı kanalda parça almak istedim
#0 --> B
#1 --> G
#2 --> R -->Red kırmızı kanalı


#resim[0:200,0:200, 2]  bölgenin red değerini artır
#resim[:,:, 2] = 255 
red = resim[0:400,0:400, 2]  #bölgenin red değerini al
cv2.imshow("red parçası", red)
cv2.waitKey()
cv2.destroyAllWindows()



