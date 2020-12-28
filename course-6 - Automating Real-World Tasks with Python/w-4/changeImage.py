#!/usr/bin/env python3

#from concurrent import futures

import argparse
import logging
import os
import sys 

import PIL
import PIL.Image

from tqdm import tqdm

images_dir_path = os.path.join(os.getcwd(), "supplier-data/images")

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def process_file(root, filename):
    filename_fullpath = os.path.join(root,filename)
    image = PIL.Image.open(filename_fullpath)
    #basename = filename.split(".")
    image.convert('RGB').resize((3000,2000)).save(os.path.join(images_dir_path,"{}.jpeg".format(filename.split('.')[0])), "JPEG")

def main():

    for root, _, files in os.walk(images_dir_path):
        for basename in progress_bar(files):
            if basename.endswith(".tiff"):
                process_file(root, basename)
    print('Waiting for all threads to finish.')
    return 0

if __name__ == "__main__":
    sys.exit(main())