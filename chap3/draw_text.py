import cv2

try:
  img = cv2.imread('img/Lenna.jpg')
  if img is None:
    print('ファイルを読み込めません')
    import sys
    sys.exit()
  
  # 画像に対して文字を描く
  cv2.putText(img, 'Hello OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
     (150, 60, 80), 2)
  cv2.imwrite('img/puttext.jpg', img)
  cv2.imshow('img', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

except:
  import sys
  print("Error:", sys.exc_info()[0])
  print(sys.exc_info()[1])
  import traceback
  print(traceback.format_tb(sys.exc_info()[2]))