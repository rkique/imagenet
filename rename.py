def txt_to_list(path):
    txt_file = open(path, 'r', encoding="utf-8")
    txt = txt_file.readlines()
    txt = [x.strip() for x in txt]
    return txt

# indices = txt_to_list("index.txt")
# i = {}
# for indice in indices:
#     i[indice.split(",")[0]] = indice.split(",")[1]

import os 
import shutil

shared = txt_to_list("shared.txt")
print(shared)

shared = [k for k in shared if k > "ice"]
folders = next(os.walk('D:\ImageNet\imagenet21k_resized\imagenet21k_train'))[1]
for folder in folders:
    if(folder in shared):
        shutil.copyfile(f'D:\ImageNet\imagenet21k_resized\imagenet21k_train\{folder}\\' + os.listdir('D:\ImageNet\imagenet21k_resized\imagenet21k_train\\'+folder)[0], 'images/'+folder+'.jpeg')
