from multiprocessing.spawn import import_main_path


import os
from PIL import Image
def txt_to_list(path):
    with open(path, 'r') as f:
        txt = f.readlines()
        txt = [x.strip() for x in txt]
        return txt

shared = txt_to_list('shared.txt')
images = os.listdir('sqm_averages')
print(images)
for image in images:
    if image.split('.')[0] in shared:
        im = Image.open('sqm_averages/'+image)
        im2 = im.copy()
        im2.save('prod_sqm_averages/'+image)
