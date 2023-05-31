import tkinter as tk
from PIL import ImageTk, Image
import cv2

class VideoPlayer:
    def __init__(self, video_path, window):
        self.video_path = video_path
        self.window = window
        self.playing = False

        self.canvas = tk.Canvas(window, width=1280, height=720)
        self.canvas.pack()

        self.play_button = tk.Button(window, text="Play", command=self.toggle_play)
        self.play_button.pack()

        self.cap = None
        self.total_frames = 0

    def toggle_play(self):
        self.playing = not self.playing
        if self.playing:
            if not self.cap:
                self.cap = cv2.VideoCapture(self.video_path)
                self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.play_video()

    def play_video(self):
        current_frame = 0  # 現在のフレーム数
        while self.playing and current_frame < self.total_frames:
            ret, frame = self.cap.read()
            if not ret:
                self.playing = False
                break

            # OpenCVのBGR画像をPillowのRGB画像に変換
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # サイズをウィンドウの大きさにリサイズ
            resized_image = image.resize((1280, 720))
            # Pillowの画像をTkinterのImageTkオブジェクトに変換
            photo = ImageTk.PhotoImage(resized_image)

            # キャンバスに表示
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.window.update()

            current_frame += 1

        if current_frame >= self.total_frames:
            self.cap.release()
            self.cap = None
        print("play_end")


# Tkinterウィンドウを作成
window = tk.Tk()
window.title("Video Player")

# 動画プレーヤーを作成
player = VideoPlayer("/home/delltkw109u/work/pytest/mp4/dualHA_BSH2.mp4", window)

# ウィンドウを表示
window.mainloop()
