import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="bird.jpg"
    rgb=plt.imread(img_path)
    red=rgb[:,:,0]
    green=rgb[:,:,1]
    blue=rgb[:,:,2]
    w,h=red.shape
    grayscale=np.zeros((w,h),dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            grayscale[i][j]=0.299*red[i][j]+0.587*green[i][j]+0.114*blue[i][j]
    plt.subplot(1,3,1)
    plt.imshow(rgb)
    plt.title("RGB Image")

    plt.subplot(1,3,2)
    plt.imshow(grayscale,cmap="gray")
    plt.title("Grayscale Image")
    w,h=grayscale.shape
    binary=np.zeros((w,h),dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            if(grayscale[i][j]>127):
                binary[i][j]=255
            else:
                binary[i][j]=0
    
    
    w,h=grayscale.shape
    s1=np.zeros((w,h),dtype=np.uint8)
    input=grayscale.max()
    c=255/(np.log(1+input))
    for i in range(w):
        for j in range(h):
            s1[i][j]=c*np.log(1+grayscale[i][j])


    
    s2=np.zeros((w,h),dtype=np.uint8)
    gamma=0.4
    for i in range(0,w):
        for j in range(0,h):
            s2[i][j]=(c*grayscale[i][j])**gamma
            
    
    s3=np.zeros((w,h),dtype=np.uint8)
    for i in range(0,w):
        for j in range(0,h):
            s3[i][j]=255-grayscale[i][j]
    
    s4=s2
    h1=h/2
    w1=w/2
    
    for i in range(0,w):
        for j in range(0,h):
            if(i<=w1 and j<=h1):
                s4[i][j]=binary[i][j]
            elif(i<=w1 and j>=h1):
                s4[i][j]=s1[i][j]
            elif(i>=w1 and j<=h1):
                s4[i][j]=s2[i][j]
            else:
                s4[i][j]=s3[i][j]

    plt.subplot(1,3,3)
    plt.imshow(s4,cmap="gray")
    plt.title("S4 Image")


    plt.show()






if __name__=='__main__':
    main()