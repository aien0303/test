import os
from PIL import ImageFile
import glob
import cv2
 
basewidth=640
filename=0

all_image_files = glob.glob('images/*.jpg')
output_dir = "resized_images"
ImageFile.LOAD_TRUNCATED_IMAGES = True
 
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
for image_file in all_image_files:
    print("Processing", image_file, "...")
    img=cv2.imread(image_file)
    reimg=cv2.resize(img,(640,360))
    filename=str(filename)
    print("Save to "+filename)
    cv2.imwrite('resized_images/'+filename+'.jpg',reimg)
    filename=int(filename)+1