import numpy as np
import cv2
import matplotlib.pyplot as plt

#recupere les images
img1 = cv2.imread('d3.jpg',0)
img2 = cv2.imread('d2.jpg',0)
# D1 - D3 = 121
# D1 - D2 = 133
# D2 - D3 =

# definition du detecteur
orb = cv2.ORB_create()

#recherche des points clef entre les deux img
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

#bfMatcher = brute Force Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

#recherche des similarites
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

# on affiche les img avec les 10 premieres similarites
print(len(matches))
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
# cv2.imshow('similarity', img3)
# cv2.waitKey()
plt.imshow(img3)
plt.show()
