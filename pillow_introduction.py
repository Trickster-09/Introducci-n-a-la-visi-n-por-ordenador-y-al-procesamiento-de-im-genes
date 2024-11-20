#Question 1: 
#Use the image `lenna.png` from this lab or take any image you like.
#Open the image and create a PIL Image object called `blue_lenna`,
# convert the image into a numpy array we can manipulate called `blue_array`, get the blue channel out of it, and finally plot the image

# write your code here

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

my_image = "lenna.png"
image = Image.open(my_image)
array= np.asarray(image)
baboon_blue=array.copy()
baboon_blue[:,:,0] = 0
baboon_blue[:,:,1] = 0
plt.figure(figsize=(10,10))
plt.imshow(baboon_blue)
plt.show()