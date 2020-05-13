import numpy as np
import matplotlib.pyplot as plt
import scipy
from lr_utils import load_dataset
import os, numpy
from PIL import Image
from scipy import ndimage


# Access all PNG files in directory
allfiles=os.listdir(os.getcwd())
image_list=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]

# Assuming all images are the same size, get dimensions of first image
width,height=Image.open(image_list[0]).size
N=len(image_list)

# Create a numpy final_arrayay of floats to store the average 
# Assume RGBA images)
final_array=numpy.zeros((height,width,4),numpy.float)

# Build up average pixel intensities, casting each image as an final_arrayay of floats
for i in range(0,len(image_list)):
    print(i)
    imfinal_array=numpy.array(Image.open(image_list[i]),dtype=numpy.float)
    #imfinal_array.reshape( imfinal_array.shape[0], 1 ).T
    #print(imfinal_array.shape)
    final_array=final_array+imfinal_array/N

# Round values in final_arrayay and cast as 8-bit integer
final_array=numpy.array(numpy.round(final_array),dtype=numpy.uint8)

# Generate, save and preview final image
out=Image.fromarray(final_array,mode="RGBA")
out.save("Average.png")
out.show()