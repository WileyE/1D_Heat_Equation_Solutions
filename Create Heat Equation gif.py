#imports
from os import getcwd
from os import walk
import imageio


#Get png files w/o extension
images = []
for root,dirs,files in walk(getcwd()):
    for filename in files:
        if filename.find('.png') > 1:
            images.append(int(filename[0:filename.find('.png')]))


#Sort on the number
sorted_images = sorted(images)             


#add the extension
final_list = []
for image in sorted_images:
    final_list.append(str(image) + '.png')
    

#Read images
image_list = []
for file_name in final_list:
    image_list.append(imageio.imread(file_name))
    
    
#Create GIF
imageio.mimwrite('Heat Equation gif.gif',image_list,duration = .25)
            