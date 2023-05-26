# アナログメーター
# The same but without the fading effect for the arrow
# coding: utf-8
import tkinter as tk #Python3
from math import pi, cos, sin


class Meter(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)
        self.var = tk.IntVar(self, 0)
        self.canvas = tk.Canvas(self, width=200, height=110,borderwidth=2, relief='sunken',bg='white')
        self.scale = tk.Scale(self, orient='horizontal',from_=0, to=100, variable=self.var)
        self.meter = self.canvas.create_line(100, 100, 10, 100,fill='black',width=3,arrow='last')
        self.angle = 0
        self.updateMeterLine(0.2)
        self.canvas.create_arc(10, 10, 190, 190, extent=108, start=36,style='arc', outline='red')
        self.canvas.pack(fill='both')
        self.scale.pack()
        self.var.trace_add('write', self.updateMeter)

    def updateMeterLine(self, a):
        """Draw a meter line"""
        self.angle = a
        x = 100 - 90 * cos(a * pi)
        y = 100 - 90 * sin(a * pi)
        self.canvas.coords(self.meter, 100, 100, x, y)

    def updateMeter(self, name1, name2, op):
        """Convert variable to angle on trace"""
        mini = self.scale.cget('from')
        maxi = self.scale.cget('to')
        pos = (self.var.get() - mini) / (maxi - mini)
        self.updateMeterLine(pos * 0.6 + 0.2)


if __name__ == '__main__':
    root = tk.Tk()
    meter = Meter(root)
    meter.pack()
    root.mainloop()
