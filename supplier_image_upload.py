#!/usr/bin/env python3
"""Upload the image to webserver using requests module"""
import requests
import glob

url = "http://35.222.32.9/upload/"
for image in glob.iglob(r"../supplier-data/images/*.jpeg"):
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
