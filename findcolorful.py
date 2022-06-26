from PIL import Image
import os
import shutil
# look at the images in a subdirectory of imagenet... 

# retrieve all images from subdirectory and do something to all of them

#shutil.copytree(r"D:\ImageNet\imagenet21k_resized\imagenet21k_train\airplane", r'C:\Users\Eric\Desktop\imagenet\airplane')

images = os.listdir(r'C:\Users\Eric\Desktop\imagenet\airplane')
for path in images:
    with Image.open(path) as image:
        image.rotate(45).show()

# for f in folders[100]:
#     shutil.copyfile(f'D:\ImageNet\imagenet21k_resized\imagenet21k_train\{folders[100]}\\{f}' + os.listdir('D:\ImageNet\imagenet21k_resized\imagenet21k_train\\'+f)[0], 'images/image-class/'+f+'.jpeg')

# 
# images that don't have white or clear backgrounds

# take the average by pixel color image from each subdirectory
