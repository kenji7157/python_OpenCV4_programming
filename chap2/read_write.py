import cv2

# 画像情報の読み込み
img = cv2.imread('img/Lenna.jpg')
# 画像情報の保存(書き込み)
cv2.imwrite('img/ReadWrite.jpg', img)