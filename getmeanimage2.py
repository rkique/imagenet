

#use the better method to get the mean image for alarm clock
from PIL import Image
import numpy as np
import os
#given our directory, we will use os.listdir() to retrieve all images
paths = os.listdir(r"D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\amphora")
print(paths[20])

average_image = np.empty((200,200,3))
errors = 0
for path in paths:
    with Image.open(r"D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\amphora\\"+path) as image:
        image.thumbnail((200,200))
        try:
            #(200,200,3) of RGB values, 
            this_image_squared = np.square(np.array(image), dtype=np.float16)
            #print(this_image_squared)
            average_image+=this_image_squared
        except ValueError:
            errors+=1
            pass
        #print(p_avg/200)
    #divide pixel values
print(f'there were {len(paths)} images and {errors} errors')
#(200,200,3) average image array for each of the values, divide it by (1027) (the number of images)
print(average_image)
data = (average_image/len(paths))**(1/2)
print(data)
avg_image = Image.fromarray(data.astype(np.uint8))
avg_image.show()
avg_image.save('squaredmean_aiplane.jpg', "JPEG")


