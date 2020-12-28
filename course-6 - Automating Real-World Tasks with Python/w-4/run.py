
#!/usr/bin/env python3

import os
import requests
import sys
import json 

description_path = os.path.join(os.getcwd(), "supplier-data/descriptions")
api_url = "http://35.193.22.190/fruits/"

def process_file(root, filename):
    filename_fullpath = os.path.join(root,filename)
    fruit = dict()
    with open(filename_fullpath, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines] 
        fruit['name'] = lines[0]
        fruit['weight'] = int(lines[1].strip('lbs'))
        fruit['description'] = lines[2]
        fruit['image_name'] = "{}.jpeg".format(filename.split('.')[0])

    return json.dumps(fruit)

def upload_description(url, root, filename):
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    return requests.post(url, data=process_file(root, filename), headers=headers) 

def main():
    for root, _, files in os.walk(description_path):
        for filename in files:
            if filename.endswith(".txt"):
                response = upload_description(api_url, root, filename)
                print("{} uploaded with status code {}".format(filename, response.text)) 

    print('Waiting for all threads to finish.')
    return 0

if __name__ == "__main__":
    sys.exit(main())