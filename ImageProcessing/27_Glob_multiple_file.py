
# we do image processing on multiple files


import cv2
import glob



my_list = []

path = "images/*.*"

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    my_list.append(a)
    
    
    
from matplotlib import pyplot as plt
plt.imshow(my_list[3])