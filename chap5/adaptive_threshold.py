import cv2

try:
  img = cv2.imread('img/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # アダプティブスレッショルド変換
  # 周りのピクセルと比べ輝度が大きい箇所は 最大値(200)に変換
  # 周りのピクセルと比べ輝度が小さい箇所は 0に変換
  dst = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 7, 8)
  cv2.imwrite('img/adaptiveThreshold.jpg', dst)
  cv2.imshow('dst', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))