import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# Read an image file
img = cv2.imread("images/BRG.png",1)  # 0 - Grayscal, 1 - Color
print("Img size: ",img.shape)

# Check pixel values:  Blue Green Red(BRG) in OpenCV
print("Top left: ",img[0,0])
print("Top right: ",img[0,300])
print("Bottom left: ",img[300,0])
print("Bottom right: ",img[300,300]) 

# Display the image
cv2.imshow("Orginal img:",img)

# # Individual Pixel Values from NumPy Array
# blue  = img[:,:,0];
# green = img[:,:,1];
# red   = img[:,:,2];

# OR equivalently:
blue, green, red = cv2.split(img)

cv2.imshow("Blue pixels:",blue)
cv2.imshow("Green pixels:",green)
cv2.imshow("Red pixels:",red)

# Marge the channels
img_merge = cv2.merge((blue,green,red))
cv2.imshow("Marged channels:",img_merge)

# Resize Image
resize = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resize image:",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# # Ploting figure
# fig, ax = plt.subplots()
# ax.plot(t, s)
# ax.set(xlabel='time (s)', ylabel='y=sin(2\pi t)',
#        title='About as simple as it gets, folks')
# ax.grid()
# fig.savefig("test.png")
# plt.show()

# # Ploting test figure
# plt.figure()
# plt.plot(range(10), 'o')
# plt.show()
