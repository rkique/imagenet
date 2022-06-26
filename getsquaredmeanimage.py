
#use the better method to get the mean image for zuchinni

from PIL import Image
import numpy as np
import os

average_image = np.empty((200,200,3))
errors = 0
with Image.open('zucchini.jpeg') as image:
    image.thumbnail((200,200))
    npimage = np.array(image)
    print(npimage[0][0])
    print(npimage[0][1])
    print(npimage.dtype)
    npimage = np.square(npimage, dtype=np.float64)
    print(npimage[0][0])
    print(npimage[0][1])