# -*- coding: utf-8 -*-

from skimage import io
 

img = io.imread("images/Osteosarcoma_01.tif")




from skimage import filters 

gaussian_img = filters.gaussian(img,sigma=3)

from skimage import img_as_ubyte
gaussian_img_8bit = img_as_ubyte(gaussian_img)


io.imsave('images/exported/save_ufing_skimage.jpg',gaussian_img_8bit)


###################################
 
import cv2 
gausssian_img_8bit_rgb = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite('images/exported/save_ufing_skimage2.jpg',gausssian_img_8bit_rgb)