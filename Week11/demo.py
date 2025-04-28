import cv2
import matplotlib.pyplot as plt


image = cv2.imread('./jurassic-park-tour-jeep.jpg')
# the swap of color channels is only necessary for inlining a picture with matplotlib
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.title('Jurrasic Park')
plt.imshow(image, interpolation='none')