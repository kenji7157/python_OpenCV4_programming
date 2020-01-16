import numpy as np
import cv2

# 画像情報(3次元配列)の生成 (行、列、色)
img = np.zeros((400, 400, 3), np.uint8)

img[:,:] = [255, 0, 0]
# 生成したimgを指定ファイルとして保存
cv2.imwrite('img/blueImage.jpg', img)
# imgを表示
cv2.imshow('img1', img)

img[:,:] = [0, 255, 0]
cv2.imwrite('img/greenImage.jpg', img)
cv2.imshow('img2', img)

img[:,:] = [0, 0, 255]
cv2.imwrite('img/redImage.jpg', img)
cv2.imshow('img3', img)

cv2.waitKey(0)
cv2.destroyAllWindows()