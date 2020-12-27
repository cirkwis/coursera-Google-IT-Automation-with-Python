#!/usr/bin/env python3

import os
import requests
import sys

def process_file(filename):
    feedback = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines] 
        feedback['title'] = lines[0]
        feedback['name'] = lines[1]
        feedback['date'] = lines[2]
        feedback['feedback'] = lines[3]

    return feedback

def main():
    
    files = os.listdir("/data/feedback")
    for filename in files :
        if filename.endswith(".txt") == False:
            continue
        feedback = process_file("/data/feedback/{}".format(filename))
        #print(feedback)
        while True:
            response = requests.post("http://35.232.34.251/feedback/", data=feedback)
            if response.status_code != 201:
                continue
            else:
                break
    print('Waiting for all threads to finish.')
    return 0

if __name__ == "__main__":
    sys.exit(main())