#!/usr/bin/env python3


import os
from PIL import Image

#Change current directory to images containing directory
os.chdir("/home/pcvs/images")
curr_dir = os.getcwd()

#Path where image is going to save
new_path = "/opt/icons"

#Check whether path exist or not
if os.path.exists(new_path)==True:
    pass
else:
    os.mkdir(new_path)
#Iterate through each image in directory and perform required operation
#Store the Modified imgaes to /opt/icons directory

#First step is to get list of files in images directory
for root,directory,file in os.walk(curr_dir):
    filelist = file
#print(filelist)
for file in filelist:
    print(file)
    try:
        im = Image.open(file)
        #To convert .Tiff file to .jpg
        new_im =im.convert("RGB")
        new_file = os.path.join(new_path,file+".jpg")
        new_im.rotate(90).resize((128,128)).save(new_file)
        print("Modified image saved of format {} at path {}".format(Image.open(new_file).format,new_file))
    except IOError:
        print("This is not image file!")
