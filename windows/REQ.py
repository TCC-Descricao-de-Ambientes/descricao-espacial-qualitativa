#from matplotlib import pyplot as plt
#from matplotlib import ticker as plticker

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from cv2 import cv2

try:
    from PIL import Image
except ImportError:
    import Image

# Open image file
image = Image.open('windows\imgEx3.jpg')
(new_width, new_height) = (1280, 720)
image.resize((round(new_width),round(new_height)),Image.ANTIALIAS)
print(image.size)

my_dpi=100.

img = cv2.imread('windows\imgEx3.jpg', cv2.IMREAD_UNCHANGED)

# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)

ax=fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)


dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
# Set the gridding interval: here we use the major tick interval
x_interval = width/5
y_interval = height/3

loc_x = plticker.MultipleLocator(base=x_interval)
loc_y = plticker.MultipleLocator(base=y_interval)
ax.xaxis.set_major_locator(loc_x)
ax.yaxis.set_major_locator(loc_y)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-', color='r', linewidth=5)

# Add the image
ax.imshow(image)

# Find number of gridsquares in x and y direction
nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(x_interval)))
ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(y_interval)))

# Save the figure
fig.savefig('exemplo_grid.jpg')

x = 300
y = 4000

if x <= image.size[0] * 1/5:
    print('muito a esquerda')
    
elif x <= image.size[0] * 2/5:
    print('na esquerda')

elif x <= image.size[0] * 3/5:
    print('no centro')

elif x <= image.size[0] * 4/5:
    print('na direita')
        
else:
    print('muito a direita')
    
if y <= image.size[1] * 1/3:
    print('em cima')

elif y <= image.size[1] * 2/3:
    print('no meio')

else:
    print('embaixo')    
