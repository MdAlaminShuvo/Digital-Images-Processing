import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    print(img_path)
    rgb=plt.imread(img_path)

    red=rgb[:,:,0]
    gren=rgb[:,:,1]
    blue=rgb[:,:,2]
    
    r,c = red.shape
    gray=np.zeros((r,c),dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            gray[i][j]=0.299*red[i][j]+0.587*gren[i][j]+0.114*blue[i][j]

    binary=np.zeros((r,c),dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            if(gray[i][j]>127):
                binary[i][j]=255
            else:
                binary[i][j]=0
    
    img_set=[gray,binary,red,gren,blue]
    img_titles=['Grayscale','Binary','Red','Green','Blue']
    n=len(img_set)
    t=0
    for i in range(n):
        ch=len(img_set[i].shape)
        plt.subplot(5,2,t+1)
        if(ch==3):
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i],cmap='gray')

        plt.title(img_titles[i])
        t=t+1
        plt.subplot(5,2,t+1)
        plt.hist(img_set[i].ravel(),255,[0,255])
        plt.title(img_titles[i])
        t=t+1
    
    plt.show()
    


if __name__ == '__main__':
    main()