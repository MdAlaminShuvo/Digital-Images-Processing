import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    average_kernel=np.array([[1,1,1],[1,1,1],[1,1,1]])*1/9
    average_filter=cv2.filter2D(grayscale,-1,average_kernel)

    plt.subplot(4,2,1)
    plt.imshow(grayscale,cmap='gray')
    plt.title("Grayscale")

    plt.subplot(4,2,2)
    plt.imshow(average_filter,cmap='gray')
    plt.title("Average Filter")

    noisy_img=grayscale
    w,h=noisy_img.shape
    number_of_pixel=random.randint(300,10000)
    for i in range(number_of_pixel):
        y=random.randint(1,w-1)
        x=random.randint(1,h-1)
        noisy_img[y][x]=255
    number_of_pixel=random.randint(300,10000)
    for i in range(number_of_pixel):
        y=random.randint(1,w-1)
        x=random.randint(1,h-1)
        noisy_img[y][x]=0

    plt.subplot(4,2,3)
    plt.imshow(noisy_img,cmap='gray')
    plt.title("Noisy Image")

    average_nois=cv2.filter2D(noisy_img,-1,average_kernel)
    plt.subplot(4,2,4)
    plt.imshow(average_nois,cmap='gray')
    plt.title("Average Noisy Image")

    gaussian_kernel=np.array([[1,2,1],[2,4,2],[1,2,1]])*1/16
    gaussian_filter=cv2.filter2D(noisy_img,-1,gaussian_kernel)
    plt.subplot(4,2,5)
    plt.imshow(gaussian_filter,cmap='gray')
    plt.title("Gaussian Filter Image")

    median=cv2.medianBlur(noisy_img,3)
    plt.subplot(4,2,6)
    plt.imshow(median,cmap='gray')
    plt.title("Median Image")
    plt.show()



if __name__=='__main__':
    main()