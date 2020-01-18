import cv2

try:
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  SCALE = 0.5
  SCALE2 = 1.62
  # 画像の高さ・幅を取得
  height = img.shape[0]
  width = img.shape[1]

  # 画像を半分(0.5乗じる)のサイズにリサイズ
  dst = cv2.resize(img, (int(width*SCALE), int(height*SCALE)))
  cv2.imwrite('img/resize0.5.jpg', dst)
  cv2.imshow('dst1', dst)

  # 画像を1.62乗じてリサイズ
  dst = cv2.resize(img, (int(width*SCALE2), int(height*SCALE2)))
  cv2.imwrite('img/resize1.62.jpg', dst)
  cv2.imshow('dst2', dst)

  # 画像を縦を圧縮してリサイズ
  dst = cv2.resize(img, (400, 200))
  cv2.imwrite('img/resize400*200.jpg', dst)
  cv2.imshow('dst3', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))