import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)[1]

    w,h=grayscale.shape
    slice1=np.zeros((w,h),dtype=np.uint8)
    slice2=np.zeros((w,h),dtype=np.uint8)
    slice3=np.zeros((w,h),dtype=np.uint8)
    slice4=np.zeros((w,h),dtype=np.uint8)
    slice5=np.zeros((w,h),dtype=np.uint8)
    slice6=np.zeros((w,h),dtype=np.uint8)
    slice7=np.zeros((w,h),dtype=np.uint8)
    slice8=np.zeros((w,h),dtype=np.uint8)

    bit=[1,2,4,8,16,32,64,128]
    slices=[slice1,slice2,slice3,slice4,slice5,slice6,slice7,slice8]

    for i in range(len(bit)):
        for j in range(w):
            for k in range(h):
                if(grayscale[j][k] & bit[i]):
                    slices[i][j][k]=255
                else:
                    slices[i][j][k]=0
    
    images=[rgb,grayscale,binary]+slices
    img_title=['rgb','gray','binary','s1','s2','s3','s4','s5','s6','s7','s8']
    n=len(images)
    for i in range(0,n):
        ch=len(images[i].shape)
        plt.subplot(6,2,i+1)
        if(ch==3):
            plt.imshow(images[i])
        else:
            plt.imshow(images[i],cmap='gray')
        plt.title(img_title[i])
    plt.show()


if __name__ == '__main__':
    main()