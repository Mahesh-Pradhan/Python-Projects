
# here we use opencv  and matplot libraies for our code

import cv2
import matplotlib.pyplot as plt

# reading/loading the image using ".imread"
# the following command reads the file in the current folder and stores in memory as image
image = cv2.imread("D:\\dog.jpg")

# displaying the image using cv2.imshow
# cv2.waitkey holds the iamge winodw
# cv2.destroyallwindow removes the all prior gui windows
"""
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# We use matplotlib rather than opencv to display the image
# but before displaying it we have to conert it into the desired format

RGB_image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_image)
plt.axis(False)
plt.show()

# From here comes the converting part
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert_image=cv2.bitwise_not(grey_image)
blur_image=cv2.GaussianBlur(invert_image,(111,111),0)
invblur=cv2.bitwise_not(blur_image)
