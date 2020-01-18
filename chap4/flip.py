import cv2

try:
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # 画像を上下反転させる
  dst = cv2.flip(img, 0)
  cv2.imwrite('img/flip0.jpg', dst)
  cv2.imshow('dst1', dst)

  # 画像を左右反転させる
  dst = cv2.flip(img, 1)
  cv2.imwrite('img/flip1.jpg', dst)
  cv2.imshow('dst2', dst)

  # 画像を両軸反転させる
  dst = cv2.flip(img, -1)
  cv2.imwrite('img/flip-1.jpg', dst)
  cv2.imshow('dst3', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))