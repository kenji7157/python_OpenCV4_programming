import cv2

try:
  # 輝度に対してスレッショルド処理を行うため、グレイスケール化
  img = cv2.imread('img/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # スレッショルド変換 (対象画像, 閾値, 最大値, スレッショルド変換設定)
  # THRESH_BINARY の場合
  # 輝度が閾値より大きい箇所は 最大値(200)に変換
  # 輝度が閾値以下の箇所は 0に変換
  ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)
  cv2.imwrite('img/threshold_THRESH_BINARY.jpg', dst)
  cv2.imshow('dst1', dst)

  # THRESH_BINARY_INV の場合
  # 輝度が閾値より大きい箇所は 0に変換
  # 輝度が閾値以下の箇所は 最大値(200)に変換
  ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY_INV)
  cv2.imwrite('img/threshold_THRESH_BINARY_INV.jpg', dst)
  cv2.imshow('dst2', dst)

  # THRESH_TRUNC の場合
  # 輝度が閾値より大きい箇所は 閾値に変換
  # 輝度が閾値以下の箇所は 0に変換
  ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TRUNC)
  cv2.imwrite('img/threshold_THRESH_TRUNC.jpg', dst)
  cv2.imshow('dst3', dst)

  # THRESH_TOZERO の場合
  # 輝度が閾値より大きい箇所は 変換しない
  # 輝度が閾値以下の箇所は 0に変換
  ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO)
  cv2.imwrite('img/threshold_THRESH_TOZERO.jpg', dst)
  cv2.imshow('dst4', dst)

  # THRESH_TOZERO_INV の場合
  # 輝度が閾値より大きい箇所は 0に変換
  # 輝度が閾値以下の箇所は 変換しない
  ret, dst = cv2.threshold(img, 100, 200, cv2.THRESH_TOZERO_INV)
  cv2.imwrite('img/threshold_THRESH_TOZERO_INV.jpg', dst)
  cv2.imshow('dst5', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))