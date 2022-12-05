import matplotlib.pyplot as plt
import numpy as np
import cv2

def Get_Custom_Equalization(img):
    w,h=img.shape
    hist,bins=np.histogram(img,256,[0,266])
    cdf=hist.cumsum()
    new_img=img.copy()
    for i in range(w):
        for j in range(h):
            new_img[i,j]=np.round((cdf[img[i,j]]-cdf.min())/(w*h-cdf.min())*255)
    return new_img

def main():
    img_path= "C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    Build_Equal=cv2.equalizeHist(grayscale)
    Custom_Equal=Get_Custom_Equalization(grayscale)

    plt.subplot(3,2,1)
    plt.imshow(grayscale,cmap='gray')
    plt.title("Main Img")

    plt.subplot(3,2,2)
    plt.hist(grayscale.ravel(),256,[0,256])
    plt.title("Main Img Histogram")

    plt.subplot(3,2,3)
    plt.imshow(Build_Equal,cmap='gray')
    plt.title("Build Equalization")

    plt.subplot(3,2,4)
    plt.hist(Build_Equal.ravel(),256,[0,256])
    plt.title("Build Histogram")

    plt.subplot(3,2,5)
    plt.imshow(Custom_Equal,cmap='gray')
    plt.title("Custom Equalization")

    plt.subplot(3,2,6)
    plt.hist(Custom_Equal.ravel(),256,[0,256])
    plt.title("Custom Histogram")
    plt.show()


if __name__=='__main__':
    main()