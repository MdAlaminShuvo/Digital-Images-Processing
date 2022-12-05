import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    img_path= "C:/Users/Dell/Desktop/class4_1/DIP/code/bird.jpg"
    rgb=plt.imread(img_path)
    grayscale=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

    plt.subplot(2,2,1)
    plt.imshow(grayscale,cmap='gray')
    plt.title('Main Image')

    fft=np.fft.fft2(grayscale)
    fft_shift=np.fft.fftshift(fft)
    mag_fft=20*np.log(np.abs(fft_shift))

    plt.subplot(2,2,2)
    plt.imshow(mag_fft,cmap='gray')
    plt.title('Magnitude FFT')

    w,h=grayscale.shape
    nw,nh=w//2,h//2
    mask=np.zeros((w,h))
    mask[nw-200:nw+200,nh-200:nh+200]=1

   
    ifft=np.fft.ifftshift(fft_shift*mask)
    ifft=np.fft.ifft2(ifft)
    mag_ifft=20*np.log(np.abs(ifft))

    plt.subplot(2,2,3)
    plt.imshow(mag_ifft,cmap='gray')
    plt.title('Magnitude IFFT')

    fft=np.fft.fft2(mag_ifft)
    fft_shift=np.fft.fftshift(fft)
    mag_fft=20*np.log(np.abs(fft_shift))

    plt.subplot(2,2,4)
    plt.imshow(mag_fft,cmap='gray')
    plt.title('Magnitude FFT')
    plt.show()

if __name__=='__main__':
    main()