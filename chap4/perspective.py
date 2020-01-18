import cv2
import numpy as np

try:
  # (225 * 225)の画像
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # 画像の列・行の大きさを取得
  rows,cols = img.shape[:2]
  x0 = cols/4
  x1 = (cols*3)/4
  y0 = rows/4
  y1 = (rows*3)/4

  # 入力の座標を指定
  list_srcs = np.float32([
    [x0, y0],
    [x0, y1],
    [x1, y1],
    [x1, y0]
  ])

  # pattern-0
  x_margin = cols/10
  y_margin = rows/10

  # 出力の座標を指定(台形)
  list_dsts = np.float32([
    [x0+x_margin, y0+y_margin],
    list_srcs[1],
    list_srcs[2],
    [x1-x_margin, y0+y_margin]
  ])
  # 透視変換行列の生成 (入力座標, 出力座標)
  perspective_matrix = cv2.getPerspectiveTransform(list_srcs, list_dsts)
  # 画像の透視投影処理 (対象画像, 透視変換行列, 出力配列(画像サイズの指定))
  dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
  cv2.imwrite('img/dst0.jpg', dst)
  cv2.imshow('dst0', dst)

  #pattern-1
  x_margin = cols/8
  y_margin = rows/8
  list_dsts = np.float32([list_srcs[0],list_srcs[1],[x1-x_margin, y1-y_margin],[x1-x_margin, y0+y_margin]])
  perspective_matrix = cv2.getPerspectiveTransform(list_srcs,list_dsts)
  dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
  cv2.imwrite('img/dst1.jpg', dst)
  cv2.imshow('dst1', dst)

  #pattern-2
  x_margin = cols/6
  y_margin = rows/6
  list_dsts = np.float32([[x0+x_margin, y0+y_margin],list_srcs[1],[x1-x_margin, y1-y_margin],list_srcs[3]])
  perspective_matrix = cv2.getPerspectiveTransform(list_srcs,list_dsts)
  dst = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
  cv2.imwrite('img/dst2.jpg', dst)
  cv2.imshow('dst2', dst)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))