#!/usr/bin/env python3
"""A script for resizing and converting images
into jpeg file with 600x400 pixel resolution."""

import os, glob
from PIL import Image

#Loop through the image directory
for image in glob.iglob(r"../supplier-data/images/*.tiff"):

    #Create Image object for processing
    with Image.open(image) as im:

        #Change the mode of the image to RGB mode
        im = im.convert("RGB")

        #Resize the image to 600x400 pixel resolution
        new_im = im.resize((600, 400))

        #Convert and save the image into jpeg file
        outfile = "../supplier-data/images/" + os.path.basename(image).split(".")[0] + ".jpeg"
        new_im.save(outfile, "JPEG")
