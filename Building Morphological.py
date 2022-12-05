import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/mor.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)

    kernel1=np.ones((3,3),dtype=np.uint8)
    kernel2=np.ones((5,5),dtype=np.uint8)
    kernel3=np.ones((7,7),dtype=np.uint8)

    erod1=cv2.erode(binary,kernel1,iterations=1)
    dilate1=cv2.dilate(binary,kernel1,iterations=1)
    open1=cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel1)
    close1=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel1)

    erod2=cv2.erode(binary,kernel2,iterations=1)
    dilate2=cv2.dilate(binary,kernel2,iterations=1)
    open2=cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel2)
    close2=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel2)

    erod3=cv2.erode(binary,kernel3,iterations=1)
    dilate3=cv2.dilate(binary,kernel3,iterations=1)
    open3=cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel3)
    close3=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel3)

    images=[erod1,dilate1,open1,close1,erod2,dilate2,open2,close2,erod3,dilate3,open3,close3]
    title=['Erosion1','Dilation1','Opening1','Closing1','Erosion2','Dilation2','Opening2','Closing2','Erosion3','Dilation3','Opening3','Closing3']

    n=len(images)

    for i in range(n):
        plt.subplot(6,2,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(title[i])
    plt.show()



if __name__=='__main__':
    main()