import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

my_img = cv2.imread('Assets\\penguen.jpg',1)
print(my_img.shape)
print(f"Görüntü Yüksekliği: {my_img.shape[0]}")
print(f"Görüntü Genişliği: {my_img.shape[1]}")
# print(f"Görüntü Kanal Sayısı: {my_img.shape[2]}") 

img_rgb = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()

img_gray_1=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray_1,cmap ='gray')
plt.axis('off')
plt.show()

print(img_rgb.shape)
print(img_gray_1.shape)

print(f"RGB görüntünün piksel değeri: {img_rgb[100,100]}")
print(f"RGB görüntünün piksel değeri: {img_gray_1[100,100]}")

figur = plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.axis('off')
plt.title('RGB Image')
plt.subplot(1,2,2)
plt.imshow(img_gray_1,cmap='gray')
plt.axis('off')
plt.title('Gray Image')
plt.show()

# plt.tight_layout()
# plt.savefig('Assets\\gray_penguen.png'dpi=300)
# cv2.imwrite('Assets\\gray_penguen.png',img_gray_1)
print(f"Görüntüde yer alan en düşük piksel değeri: {np.max(img_rgb)}")
print(f"Görüntüde yer alan en düşük piksel değeri: {np.min(img_rgb)}")

img_rgb_2=img_rgb/255.0

print(f"Görüntüde yer alan en düşük piksel değeri: {np.max(img_rgb_2)}")
print(f"Görüntüde yer alan en düşük piksel değeri: {np.min(img_rgb_2)}")




