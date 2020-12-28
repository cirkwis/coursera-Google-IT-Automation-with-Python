#!/usr/bin/env python3

import json
import locale
import sys
import os
import emails
import reports
from datetime import date

today = date.today()

description_path = os.path.join(os.getcwd(), "supplier-data/descriptions")

def process_file(root, filename):
    filename_fullpath = os.path.join(root,filename)
    fruit = dict()
    with open(filename_fullpath, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines] 
        fruit['name'] = lines[0]
        fruit['weight'] = lines[1]

    return "name: {}<br />weight: {}".format(fruit['name'], fruit['weight'])

def main(argv):
    summary = []
    for root, _, files in os.walk(description_path):
        for filename in files:
            if filename.endswith(".txt"):
                fruit_str = process_file(root, filename)
                summary.append(fruit_str)
    summary_str = "<br /><br />".join(summary)
    reports.generate_report("/tmp/processed.pdf", "Processed Update on {}".format(today), summary_str)
  

  # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
