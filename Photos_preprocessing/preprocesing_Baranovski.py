import cv2
# Type: pip install opencv-python in terminal to install cv package.
import os

''' First thing to do is to crop images from phototeodolite to get rid of this black frame, 
information described on the frame would be save and extract.
I'm aware that with this num of images I could simply just do the cropping with photoshop,
but there could be in difrent shape when croping it manually and I want images to be same size each,
and maybe there is a lot of more
phototeodolit photos that could be proceed with that code.
Also I want to learn some openCV :D 

IMAGE PROPERTIES: 2046 x 2833 x 3
'''


# Create list of image files in directory
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


baranovski_16_08_82 = load_images_from_folder('D:\Spitsbergen\SFM_Archival_Photogrametry\Images\82_08_16')
baranovski_17_08_82 = load_images_from_folder('D:\Spitsbergen\SFM_Archival_Photogrametry\Images\82_08_17')

## Checking the shape of images
# for i in range(6):
#     print(f"{baranovski_16_08_82[i].shape} --- 16.08.82")
#     print(f"{baranovski_17_08_82[i].shape} --- 17.08.82")

''' All of the image are 2046 px x 2833 px x 3 chanels '''

## Display the image.
# cv2.imshow("Example",baranovski_17_08_82[0])
# cv2.waitKey(0)

## Image to big for window to display :( -- resizing the window.
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image',2900,2050)
#
# cv2.imshow("image",baranovski_17_08_82[0])
# cv2.waitKey(0)

'''Now, when we can display whole image to find coordinates for ROI(region of interest)'''

#todo: 1) Find coordinates for cropping. 2) Crop images 3) Apply some filters to normalize images --- According to Ms.Geyman's work.
