# Basic GUI - Excersice
# Display the image below to the right hand side where the 0 is going to be ' ',
# and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
#nested for loop needed for this
for image in picture:
  for pixel in image:
    if pixel == 0:
      print(' ', end='')
    else:
      print('*',end='')
  print()