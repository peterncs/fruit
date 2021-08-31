#! /usr/bin/env python3
import os
import requests

#List all the files in /supplier-data/descriptions
for root, dirs, files in os.walk("../supplier-data/descriptions"):
    #Loop through the list of description files of fruits
    for file_name in files:
        with open(os.path.join(root,file_name)) as file:
            #Read through lines of the description file
            reader = file.readlines()
            #Store name, weight, description and image name in a dictionary
            description = {"name": reader[0],
                        "weight": int(reader[1].split(" ")[0]),
                        "description": reader[2],
                        "image_name": file_name.split(".")[0] + ".jpeg"
                        }
            #POST the dictionary to the webserver in JSON format
            response = requests.post("http://35.222.32.9/fruits/", json=description)
            response.raise_for_status()
