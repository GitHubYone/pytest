import cv2
#import numpy
#import PIL
#上下左右反転などはnumpy及びpillowでもある

# Video
#frameWidth = 800
#frameHeight = 480
#frameWidth = 320
#frameHeight = 240
frameWidth = 800
frameHeight = 600
#Video Source
#cap = cv2.VideoCapture('videos/traffic.mp4') #自分のmp4のpathを入力
cap = cv2.VideoCapture(0)
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size =(cap_width,cap_height)
num_of_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(cap_width,cap_height,num_of_frame,fps)
w = cap_width
h = cap_height

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    #img2 = cv2.flip(img,0)     # 上下反転
    img2 = cv2.flip(img,1)      # 左右反転
    #img2 = cv2.flip(img,-1)    # 上下左右反転
    #img2 = img
    #dst = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)#時計回り90度回転
    #dst = cv2.rotate(img2, cv2.ROTATE_90_COUNTERCLOCKWISE)#反時計回り90度回転
    #dst = cv2.rotate(img2, cv2.ROTATE_180)#180度回転
    dst = img2
    dst2 = cv2.resize(dst[60:-60, 80:-80, :], dsize = (w, h))
    #dst2 = dst
    cv2.imshow('Video', dst2)
    #print('ret=', ret)

    # qを押すと止まる。
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pillow, NumPy, OpenCVのそれぞれの位置づけは
# Pillow(PIL): 画像処理ライブラリ
# NumPy: 科学計算ライブラリ
# OpenCV: コンピュータビジョンライブラリ
# なので、得意分野・守備範囲に違いがある。

# 基本的には以下のように使い分けられる。
# Pillow(PIL)
# リサイズやトリミングなどの基本的な処理を行いたい場合
# NumPy ( + Pillow or OpenCV)
# 画素値ごとに算術演算などの処理を行いたい場合
# 画像をNumPyの配列ndarrayとして読み込んで計算・操作する
# NumPy単体で画像ファイルを読み込むことはできないので、PillowやOpenCVなどと併用する
# OpenCV
# ndarrayの処理に加えて、顔認識などコンピュータビジョン系の処理を行いたい場合