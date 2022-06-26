from PIL import Image
from collections import namedtuple
from operator import attrgetter
import os
def is_white(filename):
    img = Image.open(filename)
    img.thumbnail((200,200))
    w, h = img.size
    rgb1 = img.getpixel((0,0))
    rgb2 = img.getpixel((0,h-1))
    rgb3 = img.getpixel((w-1,0))
    rgb4 = img.getpixel((,h-1))
    if(sum()

is_white('zucchini.jpeg')

