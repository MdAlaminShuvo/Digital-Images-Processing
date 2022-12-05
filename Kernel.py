import matplotlib.pylab as plt
import numpy as np
import cv2

def main():
    img_path= "C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    img = plt.imread(img_path)
    grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


    kernel1=np.ones((3,3),dtype=np.uint8)*(1/4)
    kernel2=np.ones((3,3),dtype=np.uint8)*(9/45)
    kernel3=np.ones((3,3),dtype=np.uint8)*(7/67)
    kernel4=np.ones((3,3),dtype=np.uint8)*(1/7)
    kernel5=np.ones((3,3),dtype=np.uint8)*(1/22)
    kernel6=np.ones((3,3),dtype=np.uint8)*(1/6)

    img1=cv2.filter2D(grayscale,-1,kernel1)
    img2=cv2.filter2D(grayscale,-1,kernel2)
    img3=cv2.filter2D(grayscale,-1,kernel3)
    img4=cv2.filter2D(grayscale,-1,kernel4)
    img5=cv2.filter2D(grayscale,-1,kernel5)
    img6=cv2.filter2D(grayscale,-1,kernel6)

    images=[img,grayscale,img1,img2,img3,img4,img5,img6]
    img_title=['img','grayscale','img1','img2','img3','img4','img5','img6']

    n=len(images)

    for i in range(n):
        ch=len(images[i].shape)
        plt.subplot(4,2,i+1)
        if(ch==3):
            plt.imshow(images[i])
        else:
            plt.imshow(images[i],cmap='gray')
        plt.title(img_title[i])

    plt.show()



if __name__ == '__main__':
    main()