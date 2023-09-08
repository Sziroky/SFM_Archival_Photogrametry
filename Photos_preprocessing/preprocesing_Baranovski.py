import cv2
# Type: pip install opencv-python in terminal to install cv package.
import os
import matplotlib
import matplotlib.pyplot as plt

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

# Checking the shape of images
for i in range(3):
    print(f"{baranovski_16_08_82[i].shape} --- 16.08.82")
    print(f"{baranovski_17_08_82[i].shape} --- 17.08.82")

''' All of the image are 2046 px x 2833 px x 3 chanels '''

## Display the image.
# cv2.imshow("Example",baranovski_17_08_82[0])
# cv2.waitKey(0)

# Image to big for window to display :( -- resizing the window.


'''Now, when we can display whole image to find coordinates for ROI(region of interest)'''
cut = baranovski_16_08_82[1][153:1946, 135:2683]  # Coordinates Manually Set

'''Iterate over every Image'''
cut_images_16_08 = []
for i in baranovski_16_08_82:
    cut = i[179:1926, 135:2683]  # changing height -- not every image is correctly cropped, greater value should not
    # impact reconstruction which mainly focused on ground forms.
    cut_images_16_08.append(cut)

cut_images_17_08 = []
for i in baranovski_17_08_82:
    cut = i[179:1926, 135:2683]  # changing height -- not every image is correctly cropped, greater value should not
    # impact reconstruction which mainly focused on ground forms.
    cut_images_17_08.append(cut)

'''We cropped the images, now its time to think about filters that should be applied to get rid of noise and artefacts '''

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 2900, 2050)
# for i in range(6):
#     cv2.imshow("image", cut_images_17_08[i])
#     cv2.waitKey(0)

# todo:Apply some filters to normalize images --- According to Ms.Geyman's work.

# Let's generate image histograms to get information about pixel values in every single pic and its name.

n = 23
for img in cut_images_17_08:
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr)
    name = f"SV_1982-08-16_{n}"
    n += 1
    plt.savefig(fr'D:\SFM_Archival_Photogrametry\Images\Histograms\\{name}')

n = 13
for img in cut_images_16_08:
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr)
    name = f"SV_1982-08-16_{n}"
    n += 1
    plt.savefig(fr'D:\SFM_Archival_Photogrametry\Images\Histograms\\{name}')
    
