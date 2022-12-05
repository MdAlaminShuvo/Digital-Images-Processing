import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    img=cv2.GaussianBlur(grayscale,(3,3),0)
    laplacian=cv2.Laplacian(img,cv2.CV_64F)
    sobelX=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobleY=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    plt.subplot(3,2,1)
    plt.imshow(rgb)
    plt.title('RGB')

    plt.subplot(3,2,2)
    plt.imshow(grayscale,cmap='gray')
    plt.title('Grayscale')

    plt.subplot(3,2,3)
    plt.imshow(img,cmap='gray')
    plt.title('Original Image')

    plt.subplot(3,2,4)
    plt.imshow(laplacian,cmap='gray')
    plt.title('Laplacian')

    plt.subplot(3,2,5)
    plt.imshow(sobelX,cmap='gray')
    plt.title('SobelX')

    plt.subplot(3,2,6)
    plt.imshow(sobleY,cmap='gray')
    plt.title('SobelY')

    plt.show()


if __name__ == '__main__':
    main()