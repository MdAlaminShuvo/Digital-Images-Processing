import matplotlib.pyplot as plt
import numpy as np
import cv2

def countOne(kernel):
    _,k=kernel.shape
    cnt=0
    for i in range(k):
        for j in range(k):
            if(kernel[i][j]>0):
                cnt+=1
    return cnt

def main():
    img_path='C:\\Users\\Dell\\Desktop\\class4_1\\DIP\\code\\mor.jpg'
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    th,binary=cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)
    kernel=np.array([[1,0,1],[0,1,0],[0,1,0]],dtype=np.uint8)

    count=countOne(kernel)
    nm=binary
    w,h=binary.shape
    new_img=np.zeros(shape=(w+2,h+2))
    nw,nh=new_img.shape
    new_img[1:nw-1,1:nh-1]=nm

    _,k=kernel.shape
    new_w,new_h=nw-k+1,nh-k+1
    conv_d=np.zeros(shape=(new_w,new_h))
    conv_img=np.zeros(shape=(new_w,new_h))
    for i in range(new_w):
        for j in range(new_h):
            mat=new_img[i:i+k,j:j+k]
            temp=countOne(np.multiply(kernel,mat))
            if(count==temp):
                conv_img[i][j]=255
            else:
                conv_img[i][j]=0

    
    for i in range(0,new_w):
        for j in range(0,new_h):
            mat=new_img[i:i+k,j:j+k]
            temp=countOne(np.multiply(kernel,mat))
            if(temp>0):
                conv_d[i][j]=255
            else:
                conv_d[i][j]=0

    plt.subplot(3,2,1)
    plt.imshow(grayscale,cmap='gray')
    plt.title("grayscale")

    plt.subplot(3,2,2)
    plt.imshow(binary,cmap='binary')
    plt.title("binary")

    plt.subplot(3,2,3)
    plt.imshow(kernel,cmap='binary')
    plt.title("kernel")

    plt.subplot(3,2,4)
    plt.imshow(conv_img,cmap='gray')
    plt.title("Erosion")

    plt.subplot(3,2,5)
    plt.imshow(conv_d,cmap='gray')
    plt.title("Dilation")

    plt.show()





if __name__=='__main__':
    main()