import tkinter as tk
import cv2

def play_video(start_time):
    video_path = "/home/delltkw109u/work/pytest/mp4/dualHA_BSH2.mp4"
    cap = cv2.VideoCapture(video_path)

    # 動画の再生位置を指定
    cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video Player", frame)

        # "q"キーを押すと動画再生を終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("Video Player")

# 動画再生ボタンを作成
def play_from_start():
    play_video(0)  # 再生位置を0秒から開始

def play_from_30s():
    play_video(30)  # 再生位置を30秒から開始

play_button = tk.Button(window, text="Play from Start", command=play_from_start)
play_button.pack()

play_button2 = tk.Button(window, text="Play from 30s", command=play_from_30s)
play_button2.pack()

# ウィンドウを表示
window.mainloop()