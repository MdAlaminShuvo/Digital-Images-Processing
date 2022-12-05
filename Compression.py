import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path="C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    fft=np.fft.fft2(grayscale)
    fft_sort=np.sort(np.abs(fft.ravel()))
    n=len(fft_sort)
    i=1
    for keep in (0.75,0.50,0.1,0.05,0.01,0.001,0.0001):
        thresh=fft_sort[int(np.floor(n*(1-keep)))]
        ind=np.abs(fft)>thresh
        allow=fft*ind
        ifft=np.fft.ifft2(allow).real

        plt.subplot(4,2,i)
        plt.imshow(ifft,cmap='gray')
        plt.title("keep ={}%".format(keep*100))
        i+=1
    plt.show()


if __name__=='__main__':
    main()