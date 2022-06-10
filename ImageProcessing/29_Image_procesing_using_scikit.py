# -*- coding: utf-8 -*-




import matplotlib.pyplot as plt 

from skimage import io,color
from skimage.transform import rescale , resize , downscale_local_mean

img = io.imread("images/Osteosarcoma_01.tif")
#as gray does the floating point convertion 

img_rescaled = rescale(img,1.0/4.0,anti_aliasing=False)

img_resized = resize(img, (200,200),anti_aliasing=True)

img_downscaled = downscale_local_mean(img,4,3)

plt.imshow(img_downscaled)