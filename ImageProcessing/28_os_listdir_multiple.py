# -*- coding: utf-8 -*-

import os
'''
path="images/"

#print(os.listdir(path))


for image in os.listdir(path):
    print(image)
    
    '''
    
print(os.walk('.'))

for root,dirs,files in os.walk('.'):
    print(root)
    path = root.split(os.sep)
    print(files)