import cv2
import numpy as np
import os, os.path

imgs = []
imgsNames = []
path = os.getcwd();
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images or f == "d1.jpg":
        continue
    else:
        imgsNames.append(f)
        imgs.append(cv2.cvtColor(cv2.imread(os.path.join(path,f)), cv2.COLOR_BGR2GRAY))


histDico = {}
result = {}
resultListValue = []
resultListName = []


# test image
image = cv2.imread('d1.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0],
						None, [256], [0, 256])

for i in range(len(imgs)):
    histogram = cv2.calcHist([imgs[i]], [0],
        						None, [256], [0, 256])
    histDico[imgsNames[i]] = histogram


# Euclidean Distace between data1 and test
for name, hist in histDico.items():
    j = 0
    c1 = 0
    print(f"test sur {name}")
    while j<len(histogram) and j<len(hist):
    	c1+=(histogram[j]-hist[j])**2
    	j+= 1

    result[name] = c1**(1 / 2)

for name, key in result.items():
    resultListName.append(name)
    resultListValue.append(key)


for i in range(len(resultListName)):
    print(f"{resultListName[i]} = {resultListValue[i]}")
# print(np.sort(result))

# if(c1<c2):
# 	print("pinky2.jpg is more similar to pinky1.jpg as compare to pinky3.jpg")
# else:
# 	print("pinky3.jpg is more similar to pinky1.jpg as compare to pinky2.jpg")
