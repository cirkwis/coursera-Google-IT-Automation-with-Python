#!/usr/bin/env python3

import logging
import os
import sys 
import requests

from tqdm import tqdm
images_dir_path = os.path.join(os.getcwd(), "supplier-data/images")

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def upload_file(url, root, filename):
    filename_fullpath = os.path.join(root,filename)
    with open(filename_fullpath, 'rb') as opened:
        response = requests.post(url, files={'file': opened})
        print("{} uploaded with status code {}".format(filename, response.status_code))    

def main():
    api_url = "http://35.193.22.190/upload/"
    for root, _, files in os.walk(images_dir_path):
        for basename in progress_bar(files):
            if basename.endswith(".jpeg"):
                upload_file(api_url, root, basename)
    print('Waiting for all threads to finish.')
    return 0

if __name__ == "__main__":
    sys.exit(main())