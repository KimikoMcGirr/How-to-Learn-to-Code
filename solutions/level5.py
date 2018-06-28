# -*- coding: utf-8 -*-
import numpy as np
from os import listdir
from PIL import Image, ImageFilter
from scipy.ndimage import median_filter
from sys import argv

def process_image(infile):
    pic = Image.open(infile).convert('L')
    pic_array = np.asarray(pic, dtype=np.uint8).copy()
    pic_med = median_filter(pic_array, (5,5))
    pic_med[pic_med < pic_med.max()/2] = 0
    area = np.count_nonzero(pic_med) * 1.5**2
    return int(area)

def process_image_folder(indir):
    area_ls = [process_image(indir+f) for f in sorted(listdir(indir))]
    outfile = 'results/5.txt'
    with open(outfile, 'w') as outfile:
        outfile.write(str(area_ls))

if __name__ == '__main__':
    # input_file = 'C:/Users/sksuzuki/Documents/EXCISION/level_5/ims/'
    process_image_folder(argv[1]) #input_file)
