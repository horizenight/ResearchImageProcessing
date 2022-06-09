from skimage import io
img = io.imread("images/Osteosarcoma_01.tif",as_gray=True)



###

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img,cmap='hot')
ax1.title.set_text('1st')

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img,cmap='hot')
ax1.title.set_text('1st')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img,cmap='jet')
ax2.title.set_text('2nd')


ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img,cmap='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img,cmap='nipy_spectral')
ax4.title.set_text('4th')

