from PIL import Image
from collections import namedtuple
from operator import attrgetter
import os

def is_white(path):
    img = Image.open(path)
    w, h = img.size
    rgb1 = img.getpixel((0,0))
    rgb2 = img.getpixel((0,h-1))
    rgb3 = img.getpixel((w-1,0))
    rgb4 = img.getpixel((w-1,h-1))
    rgbs = [rgb1,rgb2,rgb3,rgb4]
    #when we read rgb1, we will convert it to a tuple of same values if it is an integer
    #print(rgbs)
    for rgb in rgbs:
        if type(rgb) is int and rgb < 250:
            return False
        if type(rgb) is tuple and sum(rgb) < 750:
            return False
    return True

fnames = os.listdir('alarm_clock')
#now, return images that fit
# 80 / 1384 of airplane images are white
# (old method) 415 / 1392 of alarm clock images are white
# (new method) 575 / 1392 of alarm clock iamges are white
# (method 3) 470 / 1392 

print(len(fnames))
ct = [fname for fname in fnames if is_white('alarm_clock/'+fname) ]
print(len(ct))

def txt_to_list(path):
    txt_file = open(path, 'r', encoding="utf-8")
    txt = txt_file.readlines()
    txt = [x.strip() for x in txt]
    return txt

import shutil

#get first image from each directory that is not white
shared = txt_to_list("shared.txt")
print(shared)

folders = next(os.walk('D:\ImageNet\imagenet21k_resized\imagenet21k_train'))[1]


for folder in folders:
    if(folder in shared):
        print(folder)
        images = os.listdir('D:\ImageNet\imagenet21k_resized\imagenet21k_train\\'+folder)
        paths = ['D:\ImageNet\imagenet21k_resized\imagenet21k_train\\'+folder+'\\'+image for image in images]
        darkpaths = [path for path in paths if not is_white(path)]
        print(f'{len(darkpaths)} dark images out of {len(paths)}' )
        shutil.copyfile(darkpaths[0], 'newdarkimages/'+folder+'.jpeg')
