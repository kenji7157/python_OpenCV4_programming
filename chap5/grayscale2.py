import cv2

try:
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # 対象画像をグレイスケールに変換 (対象画像, 白黒2値)
  dst = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
  cv2.imwrite('img/grayscale2.jpg', dst)

  cv2.imshow('img', dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))