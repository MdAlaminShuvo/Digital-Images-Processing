import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    mask_shell=np.zeros(grayscale.shape,dtype=np.uint8)
    for i in range(100,400):
        for j in range(100,500):
            mask_shell[i][j]=255
    
    img=cv2.bitwise_and(grayscale,mask_shell)

    plt.subplot(2,2,1)
    plt.imshow(rgb)
    plt.title("RGB")

    plt.subplot(2,2,2)
    plt.imshow(grayscale,cmap='gray')
    plt.title("Grayscale")

    plt.subplot(2,2,3)
    plt.imshow(mask_shell,cmap='gray')
    plt.title("Mask shell")

    plt.subplot(2,2,4)
    plt.imshow(img,cmap='gray')
    plt.title("Mask img")
    plt.show()


    
    


if __name__ == '__main__':
    main()