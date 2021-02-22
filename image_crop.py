# Improting Image class from PIL module 
from PIL import Image 
  
# Opens a image in RGB mode 
im = Image.open(r"input.png") 
  
# Setting the points for cropped image: 
# 	left being the starting edge of new image (to determine width)
# 	right being the end edge of new image (to determine width)
# 	top being the top edge of new image (to determine height)
# 	bottom being the bottom edge of new image (to determine height)

left = 0
right = 1280
top = 37
bottom = 997
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
im1.show() 

im1.save('output.png')