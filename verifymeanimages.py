import os
import shutil
from PIL import Image
import numpy as np
#verify each images has no 0 pixels

def txt_to_list(path):
    with open(path, 'r') as f:
        txt = f.readlines()
        txt = [x.strip() for x in txt]
        return txt

shared = txt_to_list("shared.txt")
images = os.listdir('sqm_averages')
print(images)

import time

def mean_squared_average2(category,paths):
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
            avg_image.save('new_sqm_averages/'+category)
            avg_image.close()
        except:
            print("error") 
            pass
        # try:
        #     avg_image.save('sqm_averages/'+category)
        # except PermissionError:
        #     mean_squared_average2(category, paths)
        # except OSError:
        #     mean_squared_average2(category, paths)
        # except ValueError:
        #     pass
        # except PermissionError:
        #     pass
        # except:
        #     print("Unknown error!")
        #     pass
    print(f'there were {len(paths)} images and {errors} errors for {category}')
    #print(f'elapsed time: {time.time()-st}')

#check for black strips
acceptable = 5000
i_ct = 0
arr = []
images = txt_to_list('badimages.txt')
images = ['hand_tool.jpg']

for image in images:
        i = Image.open('sqm_averages/' + image)
        npimage = np.array(i)
        ct = np.count_nonzero(npimage == (0,0,0))
        if(True):
            i_ct += 1
            preimage_dir_str = r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+image.split(".")[0]
            preimages = os.listdir(preimage_dir_str)
            paths = [preimage_dir_str+"\\"+preimage for preimage in preimages]
            i.close()
            arr.append(image)
            mean_squared_average2(image, paths)
        else:
            i.close()
print(f'total # of failed images is {i_ct}')
print(arr)
#print(np.shape(npimage))
