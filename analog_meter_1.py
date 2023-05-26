# アナログメーター
# the fading effect for the arrow
# coding: utf-8
import tkinter as tk  # Python3
from math import pi, cos, sin


class Meter(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)

        self.meter = []  # クラス変数
        self.angle = []  # クラス変数
        self.var = tk.IntVar(self, 0)  # スケールバー用の変数初期化

        self.canvas = tk.Canvas(self, width=200, height=110,
                                borderwidth=2, relief='sunken',
                                bg='white')
        self.scale = tk.Scale(self, orient='horizontal',
                            from_=0, to=100, variable=self.var)

        for j, i in enumerate(range(0, 100, 5)):
            # for j, i in enumerate(range(0, 100, 5)):
            # range関数は整数を順番に生成
            # range(start,stop,step) = (0,5,10,15...)
            # enumerate関数はインデックスと要素を取り出す
            # j=インデックス i=要素 (0)
            # インデックス0 要素0
            # インデックス1 要素5
            # インデックス2 要素10
            # インデックス3 要素15
            # ...
            self.meter.append(self.canvas.create_line(100, 100, 10, 100,
                                                        fill='grey%i' % i,
                                                        width=3,
                                                        arrow='last'))
            self.angle.append(0)
            self.canvas.lower(self.meter[j])    # lower背面に描画
            # self.canvas.lift(self.meter[j])
            # lift前面に描画 lineをliftすると止まっているときは灰色になってしまうのはなぜか？
            self.updateMeterLine(0.2, j)

        self.canvas.create_arc(10, 10, 190, 190, extent=108, start=36,
                                style='arc', outline='red')

        self.canvas.pack(fill='both')
        self.scale.pack()

        self.var.trace_add('write', self.updateMeter)  # なぜ？針の動いた後に陰影が残るのか？
        # この行でエラーが発生した場合は、トレースを追加する古い方法に変更してください。
        # self.var.trace（ 'w'、self.updateMeter）
        # if this line raises an error,
        # change it to the old way of adding a trace: self.var.trace('w', self.updateMeter)
        self.updateMeterTimer()

    def updateMeterLine(self, a, l=0):
        """Draw a meter line (and recurse for lighter ones...)"""
        # ドキュメンテーション文字列 関数の目的及び引数のデータ型についての説明
        # 指針を描く
        oldangle = self.angle[l]
        self.angle[l] = a
        x = 100 - 90 * cos(a * pi)
        y = 100 - 90 * sin(a * pi)
        self.canvas.coords(self.meter[l], 100, 100, x, y)
        l += 1
        if l < len(self.meter):
            self.updateMeterLine(oldangle, l)

    def updateMeter(self, name1, name2, op):
        """Convert variable to angle on trace"""
        # トレースで変数を角度に変換する
        mini = self.scale.cget('from')
        maxi = self.scale.cget('to')
        pos = (self.var.get() - mini) / (maxi - mini)
        self.updateMeterLine(pos * 0.6 + 0.2)

    def updateMeterTimer(self):
        """Fade over time"""
        # 時間とともに消える
        self.var.set(self.var.get())
        # スケールバーの値を取り込んで 1msec後に updateMeterTimer が処理される
        self.after(20, self.updateMeterTimer)


if __name__ == '__main__':
    root = tk.Tk()
    meter = Meter(root)
    meter.pack()
    root.mainloop()
