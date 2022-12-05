import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    w,h=grayscale.shape
    left=np.zeros((w,h),dtype=np.uint8)
    right=np.zeros((w,h),dtype=np.uint8)
    middle=np.zeros((w,h),dtype=np.uint8)

    for i in range(0,w):
        for j in range(0,h):
            left[i][j]=grayscale[i][j]-50
            if(left[i][j]<0):
                left[i][j]=0
    for i in range(0,w):
        for j in range(0,h):
            right[i][j]=grayscale[i][j]+80
            if(left[i][j]>255):
                right[i][j]=255
    for i in range(0,w):
        for j in range(0,h):
            middle[i][j]=(grayscale[i][j]+127)/2
            if(middle[i][j]<0):
                middle[i][j]=0
            elif(middle[i][j]>255):
                middle[i][j]=255

    plt.subplot(4,2,1)
    plt.imshow(grayscale,cmap='gray')
    plt.title('Grayscale Image')

    plt.subplot(4,2,2)
    plt.hist(grayscale.ravel(),255,[0,255])
    plt.title("Grayscale")

    plt.subplot(4,2,3)
    plt.imshow(left,cmap='gray')
    plt.title('Left Image')

    plt.subplot(4,2,4)
    plt.hist(left.ravel(),255,[0,255])
    plt.title("Left")

    plt.subplot(4,2,5)
    plt.imshow(right,cmap='gray')
    plt.title('Right Image')

    plt.subplot(4,2,6)
    plt.hist(right.ravel(),255,[0,255])
    plt.title("Right")

    plt.subplot(4,2,7)
    plt.imshow(middle,cmap='gray')
    plt.title('Middle Image')

    plt.subplot(4,2,8)
    plt.hist(middle.ravel(),255,[0,255])
    plt.title("Middle")
    plt.show()



if __name__=='__main__':
    main()