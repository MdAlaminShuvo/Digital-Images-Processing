
import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    img=np.array(grayscale)
    img=img.reshape(-1)

    yaxis=np.zeros((256,),dtype=int)
    xaxis=range(256)

    for i in range(0,len(img)):
        yaxis[img[i]]+=1

    plt.subplot(2,2,1)
    plt.bar(xaxis,yaxis,width=1)
    plt.title("Custom Histogram")

    plt.subplot(2,2,2)
    plt.hist(img.ravel(),256,[0,256])
    plt.title("Built Histogram")

    kernel=np.array([[3,0,-3],[10,0,-10],[3,0,-3]])
    conb=cv2.filter2D(grayscale,-1,kernel)
    plt.subplot(2,2,3)
    plt.imshow(conb,cmap='gray')
    plt.title("Built Filter")


    img1=grayscale
    w,h=img1.shape
    new_img=np.zeros(shape=(w+2,h+2))
    w,h=new_img.shape
    new_img[1:w-1,1:h-1]=img1
    new_img.astype(int)

    _,k=kernel.shape
    w,h=new_img.shape
    nw,nh=w-k+1,h-k+1
    conv_img=np.zeros(shape=(nw,nh))

    for i in range(nw):
        for j in range(nh):
            mat=new_img[i:i+k,j:j+k]
            conv_img[i][j]=np.sum(np.multiply(kernel,mat))
            if(conv_img[i][j]<0):
                conv_img[i][j]=0
            elif(conv_img[i][j]>255):
                conv_img[i][j]=255

    plt.subplot(2,2,4)
    plt.imshow(conv_img,cmap='gray')
    plt.title("Custom Filter")
    plt.show()


if __name__ == '__main__':
    main()