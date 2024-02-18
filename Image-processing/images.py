#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
#check pillow PIL documentaion for more functions******

from PIL import Image , ImageFilter

#img = Image.open('./Poki/pikachu.jpg')
img = Image.open('./astro.jpg') #big image

#new_img = img.resize ((400,400)) #resize but loses aspect ratio
img.thumbnail ((400,400)) #resize and keeps aspect ratio
img.save('thumbnail.jpg')






#filtered_img = img.filter(ImageFilter.BLUR) #filter object (blur)
#filtered_img = img.filter(ImageFilter.SMOOTH) #smooth img filter
#filtered_img = img.filter(ImageFilter.SHARPEN) #sharp img filter
#filtered_img = img.convert('L') #converts img to grey scale


#print(img) #prints PIL object
#print(img.format) #prints img format (which is a JPEG)
#print(img.size) #pic rez info
#print(img.mode) #RGB
#print(dir(img))

#filtered_img.save("blur.png", 'png') #saves filtered image, (filename, format)

# filtered_img.save("grey.png", 'png')
# filtered_img.show() #shows image, opens image for user to see

# rotate = filtered_img.rotate(90) #rotates img (90 degrees)
# rotate.save("grey.png", 'png')

# resize = filtered_img.resize((300,300)) #resize from 640x640(original size)  to 300x300
# resize.save("grey.png", 'png')

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box) #crops image
# region.save("grey.png", 'png')

