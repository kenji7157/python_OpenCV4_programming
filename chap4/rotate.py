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
  # 回転原点座標を生成
  center = (int(width/2), int(height/2))

  # 回転変換行列の生成 (回転原点座標, 回転角度, スケーリング値)
  affin_trans = cv2.getRotationMatrix2D(center, 33.0, 1.0)
  # 回転変換処理 (対象画像, 回転変換行列, 出力配列(画像サイズの指定))
  dst = cv2.warpAffine(img, affin_trans, (width, height))
  cv2.imwrite('img/rotate033.jpg', dst)
  cv2.imshow('dst1', dst)

  affin_trans = cv2.getRotationMatrix2D(center, 110.0, 1.2)
  dst = cv2.warpAffine(img, affin_trans, (width, height), flags=cv2.INTER_CUBIC)
  cv2.imwrite('img/rotate110.jpg', dst)
  cv2.imshow('dst2', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))