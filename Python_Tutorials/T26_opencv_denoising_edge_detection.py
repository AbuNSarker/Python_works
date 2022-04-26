import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read an image 
# img = cv2.imread("images/girl_1.png",1)  # 0 - Grayscal, 1 - Color
img = cv2.imread("images/elaine_512.png",1)  # 0 - Grayscal, 1 - Color
# img = cv2.imread("images/corrosion.png",1)  # 0 - Grayscal, 1 - Color
print("Img size: ",img.shape)

n = 5
# # Filter the image using kernel
kernel = np.ones((n,n),np.float32)/(n*n)
img_filter = cv2.filter2D(img,-1,kernel)

# # Blurring
# img_filter = cv2.blur(img,(5,5))

# # Gaussian Blurring
# img_filter = cv2.GaussianBlur(img,(5,5),0)

# # Median Blurring
# img_filter = cv2.medianBlur(img,5)

# # Bilateral Filtering
# img_filter = cv2.bilateralFilter(img,9,75,75)

# # Edges detection
img_edge = cv2.Canny(img,100,200)


# # Ploting 
plt.figure(1), plt.clf()
plt.subplot(121),plt.imshow(img),plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_filter),plt.title("Averaging")
plt.xticks([]), plt.yticks([])
plt.show()

# # Ploting figure
plt.figure(2), plt.clf()
plt.imshow(img_edge),plt.title("Edge Detection")
plt.xticks([]), plt.yticks([])
plt.show()

# # Display the image by cv2
# cv2.imshow("Orginal img:",img)
# cv2.imshow("Filtered Ima ge:",img_filter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



