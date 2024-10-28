import pillow_avif 
from PIL import Image
import numpy as np
import sys
import os

def dither_matrix(n:int):
    if n == 1:
        return np.array([[0]])
    else:
        first = (n ** 2) * dither_matrix(int(n/2))
        second = (n ** 2) * dither_matrix(int(n/2)) + 2
        third = (n ** 2) * dither_matrix(int(n/2)) + 3
        fourth = (n ** 2) * dither_matrix(int(n/2)) + 1
        first_col = np.concatenate((first, third), axis=0)
        second_col = np.concatenate((second, fourth), axis=0)
        return (1/n**2) * np.concatenate((first_col, second_col), axis=1)

def get_image(src:str):
    img = Image.open(src)
    img.thumbnail((800, 800))  # Resize the image
    img_gray = img.convert('L')  # Convert the image to grayscale
    img_arr = np.array(img_gray)  # Convert the image to a numpy array
    return img_arr * (1/255.0)  # Normalize the pixel values

def ordered_dithering(img_pixel:np.array, dither_m:np.array):
    n = np.size(dither_m, axis=0)
    x_max = np.size(img_pixel, axis=1)
    y_max = np.size(img_pixel, axis=0)
    for x in range(x_max):
        for y in range(y_max):
            i = x % n
            j = y % n
            if img_pixel[y][x] > dither_m[i][j]:
                img_pixel[y][x] = 255
            else:
                img_pixel[y][x] = 0

    Image.fromarray(img_pixel).convert('L').save(name+'_dithered.png', quality=70)

if __name__ == '__main__':
    n = 8
    src = sys.argv[1]
    name = os.path.splitext(src)[0]
    dm = dither_matrix(n)
    img = get_image(src)
    ordered_dithering(img, dm)
    print('Dithering is done \U0001F388')

    

