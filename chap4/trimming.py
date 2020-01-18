import cv2

try:
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # 画像の高さ・幅を取得
  height = img.shape[0]
  width = img.shape[1]

  # imgをスライス処理してトリミング
  dst = img[40:height, 40:width]
  cv2.imwrite('img/Trimming.jpg', dst)
  cv2.imshow('dst0', dst)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))