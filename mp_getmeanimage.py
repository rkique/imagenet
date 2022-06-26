from PIL import Image
import numpy as np
import os
import time
def mean_squared_average(paths, category):
    st = time.time()
    average_image = np.empty((200,200,3))
    errors = 0
    for path in paths:
        try:
            with Image.open(path) as image:
                image.thumbnail((200,200))
                try:
                    this_image_squared = np.square(np.array(image), dtype=np.float16)
                    average_image+=this_image_squared
                except ValueError:
                    errors+=1
                    pass
            data = (average_image/len(paths))**(1/2)
            avg_image = Image.fromarray(data.astype(np.uint8))
            avg_image.save('sqm_averages/'+category+".jpg", "JPEG")
        except: pass
    print(f'there were {len(paths)} images and {errors} errors for {category}')
    print(f'elapsed time: {time.time()-st}')

#r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category+"\\"+path

#given our directory, we will use os.listdir() to retrieve all images
categories = os.listdir(r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train')
#categories = [c for c in categories if c > "beagle"]

from multiprocessing import Pool
categories = list(categories)

def process_categories(categories):
    for category in categories:
        print(category)
        images = os.listdir(r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category)
        paths = [r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category+"\\"+image for image in images]
        mean_squared_average(paths, category)

if __name__ == '__main__':
    pool = Pool()
    pool.map(process_categories, categories)






