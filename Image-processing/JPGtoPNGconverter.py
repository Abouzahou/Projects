import sys
import os
from PIL import Image

#Run from terminal
#Command: python3 JPGtoPNGconverter.py Poki\ new \


#grab first and second argument for file path

image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if new/folder exists , and if not then create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through poki, convert the images to png
for filename in os.listdir(image_folder):
  clean_name = os.path.splitext(filename)[0] #removes name of file to convert .png, [0] = first name so we keep first name and remove .jpg 
  img = Image.open(f'{image_folder}{filename}')
  
  #added the / in case user doesn't enter it. You may want to check for this 
  #and add or remove it. 
  
  img.save(f'{output_folder}/{clean_name}.png', 'png')
  print('all done!!')


