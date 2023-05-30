import tkinter as tk
import cv2

def play_video():
    video_path = "/home/delltkw109u/work/pytest/mp4/dualHA_BSH2.mp4"
    cap = cv2.VideoCapture(video_path)

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
play_button = tk.Button(window, text="Play Video", command=play_video)
play_button.pack()

# ウィンドウを表示
window.mainloop()