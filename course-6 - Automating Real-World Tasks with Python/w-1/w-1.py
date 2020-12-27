#!/usr/bin/env python3

#from concurrent import futures

import argparse
import logging
import os
import sys 

import PIL
import PIL.Image

from tqdm import tqdm

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def process_file(root, basename):
    filename = os.path.join(root,basename)
    image = PIL.Image.open(filename)
    image.convert('RGB').rotate(-90).resize((128,128)).save(os.path.join('icons',basename), "JPEG")

def main():
    if not os.path.exists('./icons'):
        os.mkdir('./icons')

    #executor = futures.ProcessPoolExecutor()
    for root, _, files in os.walk('./images'):
        for basename in progress_bar(files):
            if basename.startswith("."):
                continue
            process_file(root, basename)
            #executor.submit(process_file, root, basename)
    print('Waiting for all threads to finish.')
    #executor.shutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())

