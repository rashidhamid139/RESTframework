# import numpy as np
# import cv2

# def center_crop(img, new_width=None, new_height=None):        
#     print(img.shape)
#     width = img.shape[1]
#     height = img.shape[0]

#     if new_width is None:
#         new_width = min(width, height)

#     if new_height is None:
#         new_height = min(width, height)

#     left = int(np.ceil((width - new_width) / 2))
#     right = width - int(np.floor((width - new_width) / 2))

#     top = int(np.ceil((height - new_height) / 2))
#     bottom = height - int(np.floor((height - new_height) / 2))

#     if len(img.shape) == 2:
#         center_cropped_img = img[top:bottom, left:right]
#     else:
#         center_cropped_img = img[top:bottom, left:right, ...]

#     return center_cropped_img

# ret =  center_crop(cv2.imread('test2.jpeg'), new_height=100, new_width=100)
# print(ret.shape)
# cv2.imshow(ret)

from PIL import Image
im = Image.open("test2.jpeg")

crop_rectangle = (50, 50, 200, 200)
cropped_im = im.crop(crop_rectangle)

cropped_im.show()