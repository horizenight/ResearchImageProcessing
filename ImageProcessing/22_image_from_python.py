from skimage import io,img_as_float

img = io.imread("images/test.png")
#read as RGB 

print(img.shape) #y , x, c


import cv2 

grey_cv2 = cv2.imread("images/test.png",0)
color_cv2 = cv2.imread("images/test.png",1)
print(grey_cv2.shape)
#open cv saves it in bgr format 

#bgr to rgb conversion 
img_opencv= cv2.cvtColor(color_cv2,cv2.COLOR_BGR2RGB)

print("exit")