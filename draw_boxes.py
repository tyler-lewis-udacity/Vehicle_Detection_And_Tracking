# Define a function that takes an image, a list of bounding boxes, 
# and optional color tuple and line thickness as inputs
# then draws boxes in that color on the output

def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # Make a copy of the image
    draw_img = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(draw_img, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return draw_img

# Here are the bounding boxes I used
bboxes = [((275, 572), (380, 510)), ((488, 563), (549, 518)), ((554, 543), (582, 522)), 
          ((601, 555), (646, 522)), ((657, 545), (685, 517)), ((849, 678), (1135, 512))]


import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#image = mpimg.imread('bbox-example-image.jpg')
image = cv2.imread('bbox-example-image.jpg', cv2.IMREAD_COLOR)#BGR
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define a function that takes an image, a list of bounding boxes, 
# and optional color tuple and line thickness as inputs
# then draws boxes in that color on the output

# Format for box: ((x1, y1), (x2, y2))
box_1 = ((), ()) # <-- (top_left_corner, top_right_corner)
#bboxes = [((100, 100), (200, 200)), ((300, 300), (400, 400))]

result = draw_boxes(image, bboxes)
#plt.imsave('bbox-example-image-out.jpg', result)# <-- Not working??
result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)# <-- ...back to BGR
cv2.imwrite('bbox-example-image-out.jpg', result)
# plt.imshow(result)
# plt.show()