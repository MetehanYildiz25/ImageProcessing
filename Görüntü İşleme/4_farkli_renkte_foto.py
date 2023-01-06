# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:32:02 2022

@author: Metehan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim=cv2.imread("araba.png")

plt.imshow(resim)
plt.show()


cv2.imshow("orjinal",resim)

print(resim.shape)

yükseklik,genişlik,kanal=resim.shape

parça1 = resim[0:int(yükseklik/2),0:int(genişlik/2)]

parça1_farklırenk = cv2.cvtColor(parça1,cv2.COLOR_BGR2GRAY)

resim[0:int(yükseklik/2),0:int(genişlik/2),0] = parça1_farklırenk


parça2 = resim[0:int(yükseklik),0:int(genişlik/2)]

parça2_farklırenk= cv2.cvtColor(parça2,cv2.COLOR_BGR2GRAY)

resim[0:int(yükseklik),0:int(genişlik/2),1] =parça2_farklırenk

parça3 =resim[0:int(yükseklik/2),0:int(genişlik)]

parça3_farklırenk=cv2.cvtColor(parça3,cv2.COLOR_BGR2GRAY)

resim[0:int(yükseklik/2),0:int(genişlik),2] =parça3_farklırenk


cv2.imshow("4 farkli renkteki foto ",resim)
cv2.waitKey()
cv2.destroyAllWindows()