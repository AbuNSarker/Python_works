# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 02:37:22 2021

@author: Admin
"""

import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# Read an image file
img = cv2.imread("images/BRG.png",1)  # 0 - Grayscal, 1 - Color
print("Img size: ",img.shape)

# Display the image
cv2.imshow("Orginal img:",img)
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
