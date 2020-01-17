import numpy as np
import cv2

# 画像データ(400×400 px)の生成
img = np.zeros((400, 400, 3), np.uint8)
# 円の描写 (対象画像データ, 中心座標, 半径, 色情報, 円の太さ)
cv2.circle(img, (200, 200), 50, (255, 0, 0) ,1)
cv2.imwrite('img/circle1.jpg', img)
cv2.imshow('img1', img)

img = np.zeros((400, 400, 3), np.uint8)
# 半径 色　太さ　を変更　
cv2.circle(img, (200, 200), 100, (0, 255, 0) ,3)
cv2.imwrite('img/circle2.jpg', img)
cv2.imshow('img2', img)

img = np.zeros((400, 400, 3), np.uint8)
# 半径 色　太さ　を変更
cv2.circle(img, (200, 200), 150, (0, 0, 255) ,-1)
cv2.imwrite('img/circle3.jpg', img)
cv2.imshow('img3', img)

cv2.waitKey(0)
cv2.destroyAllWindows()