import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    img = plt.imread(img_path)
    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    T1=50
    T2=200
    s1=np.zeros(grayscale.shape,dtype=np.uint8)
    r,c = grayscale.shape

    for i in range(r):
        for j in range(c):
            if(grayscale[i][j]>=T1 and grayscale[i][j]<=T2):
                s1[i][j]=100
            else:
                s1[i][j]=10

    plt.subplot(2,2,1)
    plt.title('First Condition')
    plt.imshow(s1,cmap='gray')

    s5=np.zeros(grayscale.shape,dtype=np.uint8)
    
    r,c = grayscale.shape
    for i in range(r):
        for j in range(c):
            if(grayscale[i][j]>=T1 and grayscale[i][j]<=T2):
                s5[i][j]=100
            else:
                s5[i][j]=grayscale[i][j]
            

    plt.subplot(2,2,2)
    plt.title('Second Condition')
    plt.imshow(s5,cmap='gray')

    s2 = np.zeros(grayscale.shape,dtype=np.uint8)
    c=2
    row,col = grayscale.shape
    for i in range(row): 
        for j in range(col):
            s2[i][j]=c*np.log(1+grayscale[i][j])
            
    plt.subplot(2,2,3)
    plt.title('Third Condition')
    plt.imshow(s2,cmap='gray')

    s3 = np.zeros(grayscale.shape,dtype=np.uint8)
    c=2
    p=4
    ep=0.000001
    row,col = grayscale.shape
    for i in range(row): 
        for j in range(col):
            s3[i][j]=c*(grayscale[i][j]+ep)**p
            
    plt.subplot(2,2,4)
    plt.title('Four Condition')
    plt.imshow(s3,cmap='gray')
    plt.show()
    
    



if __name__ == '__main__':
    main()