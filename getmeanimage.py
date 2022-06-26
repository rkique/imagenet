from PIL import Image
import numpy as np
import os
import time
import os.path

def mean_squared_average2(category,paths):
    if os.path.isfile("sqm_averages/"+category+".jpg"):
        return
    st = time.time()
    average_image = np.empty((200,200,3))
    errors = 0
    for path in paths:
        try:
            with Image.open(path) as image:
                image.thumbnail((200,200))
                try:
                    this_image_squared = np.square(np.array(image), dtype=np.uint32)
                    average_image+=this_image_squared
                except ValueError:
                    errors+=1
                    pass
            data = (average_image/len(paths))**(1/2)
            avg_image = Image.fromarray(data.astype(np.uint8))
            avg_image.save('sqm_averages/'+category+".jpg", "JPEG")
            # except ValueError:
            #     pass
            # except PermissionError:
            #     pass
            # except:
            #     print("Unknown error!")
            #     pass
        except:
            pass
    print(f'there were {len(paths)} images and {errors} errors for {category}')
    #print(f'elapsed time: {time.time()-st}')

#r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category+"\\"+path

def txt_to_list(path):
    with open(path, 'r') as f:
        txt = f.readlines()
        txt = [x.strip() for x in txt]
        return txt

shared = txt_to_list("shared.txt")

def run_mean_squared_average():
    #print(f'index is {index}')
    categories = os.listdir(r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train')
    categories = [c for c in categories if c in shared]
    print(len(categories))
    categories.sort()
    #print(f'first category for this process is {categories[0]}')
    for category in categories:
        try:
            images = os.listdir(r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category)
            paths = [r'D:\\ImageNet\\imagenet21k_resized\\imagenet21k_train\\'+category+"\\"+image for image in images]
            mean_squared_average2(category, paths)
        except:
            pass
import multiprocessing
import concurrent.futures

def main():
    run_mean_squared_average()

if __name__ == '__main__':
    main()
