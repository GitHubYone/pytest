# coding: utf-8
# アナログメーター デザイン修行

import sys
import tkinter as tk
from tkinter.constants import CENTER, DISABLED, NORMAL, NW, SW, E, S, W
from math import cos, pi, sin, fabs , e

class Meter(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)

        #初期化
        self.var0 = tk.IntVar(self, 0)
        self.var1 = tk.IntVar(self, 0)
        self.var2 = tk.IntVar(self, 0)
        self.var3 = tk.IntVar(self, 0)
        self.a_data = tk.StringVar(self, 0)
        self.a_sign = tk.StringVar(self, "")
        self.bl_data = tk.StringVar(self, 0)
        self.br_data = tk.StringVar(self, 0)
        self.s_data = tk.StringVar(self, 0)
        self.label1 = tk.StringVar(self, "SIDE SLIP")
        self.angle0 = 0
        self.angle1 = 0
        self.angle2 = 0
        self.angle3 = 0
        self.angle_b = 0
        self.b_type = 0
        self.panel = 0

        self.meter_fontsize = 72
        self.meter_fontpos = 1030

        self.canvas = tk.Canvas(self, # キャンバスエリア
                                #width = 1920, height = 1080,
                                width = 1920, height = 920,
                                borderwidth = 2, relief = "sunken", bg = "white")
        self.a_scale()
        self.meter0 = self.canvas.create_line(960, 1300, 960, 400,
                                    fill = "orange",
                                    width = 40,
                                    arrow = "last",
                                    arrowshape = (30, 60, 10),
                                    tag = "meterA") # 指針表示
        self.meter1 = self.canvas.create_line(960, 1300, 960, 400,
                                    fill = "lime",
                                    width = 40,
                                    arrow = "last",
                                    arrowshape = (30, 60, 10),
                                    tag = "meterB") # 指針表示
        self.meter2 = self.canvas.create_line(960, 1300, 960, 400,
                                    fill = "red",
                                    width = 30,
                                    arrow = "last",
                                    arrowshape = (30, 60, 10),
                                    tag = "meterB") # 指針表示
        self.meter3 = self.canvas.create_line(960, 1300, 960, 400,
                                    fill = "cyan",
                                    width = 30,
                                    arrow = "last",
                                    arrowshape = (30, 60, 10),
                                    tag = "meterB") # 指針表示

        self.updateMeterLine0((0.2*90/36))      # 指針の初期値
        self.updateMeterLine1((0.2*270/36))     # 指針の初期値
        self.updateMeterLine2((0.2*270/36))     # 指針の初期値
        self.updateMeterLine3((0.2*270/36))     # 指針の初期値
        self.canvas.pack()

        self.label = tk.Label(self, # メーター名称
                                textvariable = self.label1,
                                font = ("MS明朝", 48, "bold", "roman"),
                                fg = "black", bg = "grey77", width = 0, anchor = CENTER)
        self.label.place(x = 10, y = 10 , width = 1900 , height = 80)

        self.scale0 = tk.Scale(self,
                                variable = self.var0,
                                #command = ,
                                orient = tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                                length = 400,           # 全体の長さ
                                width = 10,             # 全体の太さ
                                sliderlength = 20,      # スライダー（つまみ）の幅
                                from_ = -160,           # 最小値（開始の値）
                                to = 160,              # 最大値（終了の値）
                                resolution = 1,           # 変化の分解能(初期値:1)
                                tickinterval = 0          # 目盛りの分解能(初期値0で表示なし)
                                )
        self.scale0.pack(side = tk.TOP)

        self.scale11 = tk.Scale(self,
                                variable = self.var1,
                                #command = ,
                                orient = tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                                length = 400,           # 全体の長さ
                                width = 10,             # 全体の太さ
                                sliderlength = 20,      # スライダー（つまみ）の幅
                                from_ = -50,           # 最小値（開始の値）
                                to = 3100,              # 最大値（終了の値）
                                resolution = 1,           # 変化の分解能(初期値:1)
                                tickinterval = 0          # 目盛りの分解能(初期値0で表示なし)
                                )
        self.scale11.pack(side = tk.TOP)

        self.scale12 = tk.Scale(self,
                                variable = self.var2,
                                #command = ,
                                orient = tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                                length = 400,           # 全体の長さ
                                width = 10,             # 全体の太さ
                                sliderlength = 20,      # スライダー（つまみ）の幅
                                from_ = -50,           # 最小値（開始の値）
                                to = 3100,              # 最大値（終了の値）
                                resolution = 1,           # 変化の分解能(初期値:1)
                                tickinterval = 0          # 目盛りの分解能(初期値0で表示なし)
                                )
        self.scale12.pack(side = tk.TOP)

        self.scale13 = tk.Scale(self,
                                variable = self.var3,
                                #command = ,
                                orient = tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                                length = 400,           # 全体の長さ
                                width = 10,             # 全体の太さ
                                sliderlength = 20,# スライダー（つまみ）の幅
                                from_ = 0,           # 最小値（開始の値）
                                to = 1200,           # 最大値（終了の値）
                                resolution = 1,      # 変化の分解能(初期値:1)
                                tickinterval = 0     # 目盛りの分解能(初期値0で表示なし)
                                )
        self.scale13.pack(side = tk.TOP)

        self.button_draw = tk.Button(self, text = u'SIDE SLIP',width=15)
        self.button_draw.bind("<Button-1>", self.a_select)
        self.button_draw.place(x = 1500, y = 20)

        self.button_draw = tk.Button(self, text = u'BRAKE TESTER',width=15)
        self.button_draw.bind("<Button-1>", self.b_select)
        self.button_draw.place(x = 1620, y = 20)

        self.button_draw = tk.Button(self, text = u'SPEEDOMETER',width=15)
        self.button_draw.bind("<Button-1>", self.s_select)
        self.button_draw.place(x = 1740, y = 20)

        self.var0.trace_add("write", self.updateMeter)
        self.var1.trace_add("write", self.updateMeter)
        self.var2.trace_add("write", self.updateMeter)
        self.var3.trace_add("write", self.updateMeter)


    def a_select(self, event):
        if self.panel != 0:
            try:
                self.label_bl.place_forget()
            except:
                pass
            try:
                self.label_br.place_forget()
            except:
                pass
            try:
                self.label_s.place_forget()
            except:
                pass
            self.panel = 0
            self.a_scale()
            self.updateMeterLine0((0.2*90/36))
            self.updateMeterLine1((0.2*270/36))
            self.updateMeterLine2((0.2*270/36))
            self.updateMeterLine3((0.2*270/36))

    def b_select(self, event):
        if self.panel != 1:
            try:
                self.label_a.place_forget()
            except:
                pass
            try:
                self.label_a_sign.place_forget()
            except:
                pass
            try:
                self.label_s.place_forget()
            except:
                pass
            self.panel = 1
            self.b_low_range()
            self.updateMeterLine0((0.2*270/36))
            self.updateMeterLine1((0.2*30/36))
            self.updateMeterLine2((0.2*30/36))
            self.updateMeterLine3((0.2*270/36))
            self.label_bl = tk.Label(self,
                                    textvariable = self.bl_data, # 表示内容
                                    font = ("MS明朝", 80, "bold", "roman"), # フォントの指定
                                    fg = "lime", # 文字色
                                    bg = "black", # 背景色
                                    width = 4, # ラベルの幅
                                    anchor = "e" # 配置
                                    )
            self.label_bl.place( x= 670, y = 710)
            self.label_br = tk.Label(self,
                                    textvariable = self.br_data, # 表示内容
                                    font = ("MS明朝", 80, "bold", "roman"), # フォントの指定
                                    fg = 'red', # 文字色
                                    bg = "black", # 背景色
                                    width = 4, # ラベルの幅
                                    anchor = "e" # 配置
                                    )
            self.label_br.place(x = 1000, y = 710)

    def s_select(self, event):
        if self.panel != 2:
            try:
                self.label_a.place_forget()
            except:
                pass
            try:
                self.label_a_sign.place_forget()
            except:
                pass
            try:
                self.label_bl.place_forget()
            except:
                pass
            try:
                self.label_br.place_forget()
            except:
                pass
            self.panel = 2
            self.s_scale()
            self.updateMeterLine0((0.2*270/36))
            self.updateMeterLine1((0.2*270/36))
            self.updateMeterLine2((0.2*270/36))
            self.updateMeterLine3((0.2*30/36))
            self.label_s = tk.Label(self,
                                    textvariable = self.s_data, # 表示内容
                                    font = ("MS明朝", 80, "bold", "roman"), # フォントの指定
                                    fg = "cyan", # 文字色
                                    bg = "black", # 背景色
                                    width = 4, # ラベルの幅
                                    anchor = "e" # 配置
                                    )
            self.label_s.place(x = 700, y = 730)

    def a_scale(self):
        self.canvas.delete("b_low")
        self.canvas.delete("b_high")
        self.canvas.delete("s_scale")
        self.label1.set("SIDE SLIP")
        self.canvas.create_arc(60, 400, 1860, 2200,
                                    extent = 90, start = 45, style = "arc", outline = "black",
                                    width = 3, tag = "a_scale")
        self.canvas.create_arc(160, 500, 1760, 2100,
                                    extent = 90, start = 45, style = "arc", outline = "black",
                                    width = 3, tag = "a_scale")
        self.canvas.create_arc(200, 540, 1720, 2060,
                                    extent = 90, start = 45, style = "arc", outline = "red",
                                    width = 40, tag = "a_scale")
        self.canvas.create_arc(200, 540, 1720, 2060,
                                    extent = 30, start = 75, style = "arc", outline = "lime",
                                    width = 40, tag = "a_scale")
        for i in range(45,138,3):   # 目盛小
            self.canvas.create_line(960+(900*cos(pi/180*i)), 1300-(900*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 4,
                                    tag = "a_scale")
        for i in range(45,150,15):  # 目盛大
            self.canvas.create_line(960+(950*cos(pi/180*i)), 1300-(950*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 8,
                                    tag = "a_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*90)),
                                1300-(self.meter_fontpos*sin(pi/180*90)),
                                text = "0", font = ("", self.meter_fontsize),
                                tag = "a_scale") # ゼロ点数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*75)),
                                1300-(self.meter_fontpos*sin(pi/180*75)),
                                text = "5",font = ("", self.meter_fontsize),
                                tag = "a_scale") # IN数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*60)),
                                1300-(self.meter_fontpos*sin(pi/180*60)),
                                text = "10", font = ("", self.meter_fontsize),
                                tag = "a_scale") # IN数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*45)),
                                1300-(self.meter_fontpos*sin(pi/180*45)),
                                text = "15", font = ("", self.meter_fontsize),
                                tag = "a_scale") # IN数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*105)),
                                1300-(self.meter_fontpos*sin(pi/180*105)),
                                text = "5", font = ("", self.meter_fontsize),
                                tag = "a_scale") # OUT数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*120)),
                                1300-(self.meter_fontpos*sin(pi/180*120)),
                                text = "10", font = ("", self.meter_fontsize),
                                tag = "a_scale") # OUT数値表示
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*135)),
                                1300-(self.meter_fontpos*sin(pi/180*135)),
                                text = "15",font = ("", self.meter_fontsize),
                                tag = "a_scale") # OUT数値表示
        self.canvas.create_text(960+((self.meter_fontpos-100)*cos(pi/180*30)),
                                1300-((self.meter_fontpos-100)*sin(pi/180*30)),
                                text = "IN",font = ("", self.meter_fontsize),
                                tag = "a_scale") # IN表示
        self.canvas.create_text(960+((self.meter_fontpos-100)*cos(pi/180*150)),
                                1300-((self.meter_fontpos-100)*sin(pi/180*150)),
                                text = "OUT", font = ("", self.meter_fontsize),
                                tag = "a_scale") # OUT表示
        self.canvas.create_text(1110, 830,
                                text = 'mm/m', font = ('', self.meter_fontsize),
                                tag = "a_scale") # 単位表示
        self.canvas.tag_lower("a_scale")
        self.label_a = tk.Label(self,
                                textvariable=self.a_data, # 表示内容
                                font = ("MS明朝", 64, "bold", "roman"), # フォントの指定
                                fg = "orange", # 文字色
                                bg = "black", # 背景色
                                width = 4, # ラベルの幅
                                anchor = "e" # 配置
                                )
        self.label_a.place(x=720,y=770)
        self.label_a_sign = tk.Label(self,
                                textvariable=self.a_sign, # 表示内容
                                font = ("MS明朝", 64, "bold", "roman"), # フォントの指定
                                fg = "orange", # 文字色
                                bg = "black", # 背景色
                                width = 4 , # ラベルの幅
                                anchor = CENTER # 配置
                                )
        self.label_a_sign.place(x = 500, y = 770)

    def b_low_range(self):
        self.canvas.delete("a_scale")
        self.canvas.delete("b_high")
        self.canvas.delete("s_scale")
        self.label1.set("BRAKE TESTER (LOW RANGE)")
        self.b_type = 0
        #self.canvas.create_arc(     # 目盛外側円弧
        #                        60, 400, 1860, 2200,
        #                        extent = 120, start = 30, style = "arc", outline = "black",
        #                        width = 5, tag = "b_low")
        self.canvas.create_arc(     # 目盛内側円弧
                                160, 500, 1760, 2100,
                                extent = 120, start = 30, style = "arc", outline = "black",
                                width = 5, tag = "b_low")
        for i in range(30,160,10):  # 目盛大
            self.canvas.create_line(960+(950*cos(pi/180*i)), 1300-(950*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 12,tag = "b_low")
        for i in range(30,155,5):   # 目盛小
            self.canvas.create_line(960+(920*cos(pi/180*i)), 1300-(920*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 6,tag = "b_low")
        for i in range(30,150,1):  # 目盛小
            self.canvas.create_line(960+(900*cos(pi/180*i)), 1300-(900*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 3,tag = "b_low")
        for i in range(146,150,1):  # 目盛小赤
            self.canvas.create_line(960+(900*cos(pi/180*i)), 1300-(900*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "red", width = 3,tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*150)),
                                1300-(self.meter_fontpos*sin(pi/180*150)),
                                text = "0", font = ("", self.meter_fontsize ),
                                tag = "b_low")
        #self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*146)),
        #                        1300-(self.meter_fontpos*sin(pi/180*146)),
        #                        text = "40",font = (2", (self.meter_fontsize-8)),
        #                        tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*140)),
                                1300-(self.meter_fontpos*sin(pi/180*140)),
                                text = "100", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*130)),
                                1300-(self.meter_fontpos*sin(pi/180*130)),
                                text = "200", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*110)),
                                1300-(self.meter_fontpos*sin(pi/180*110)),
                                text = "400", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*90)),
                                1300-(self.meter_fontpos*sin(pi/180*90)),
                                text = "600", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*70)),
                                1300-(self.meter_fontpos*sin(pi/180*70)),
                                text = "800", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*50)),
                                1300-(self.meter_fontpos*sin(pi/180*50)),
                                text = "1000", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(960+((self.meter_fontpos-40)*cos(pi/180*30)),
                                1300-((self.meter_fontpos+40)*sin(pi/180*30)),
                                text = "1200", font = ("", self.meter_fontsize),
                                tag = "b_low")
        self.canvas.create_text(870, 880,
                                text = "daN", font = ('', 64),
                                tag = "b_low")
        self.canvas.create_text(1200, 880,
                                text = "daN", font = ('', 64),
                                tag = "b_low")
        self.canvas.tag_lower("b_low")

    def b_high_range(self):
        self.canvas.delete("a_scale")
        self.canvas.delete("b_low")
        self.canvas.delete("s_scale")
        self.label1.set("BRAKE TESTER (HIGH RANGE)")
        self.b_type = 1
        #self.canvas.create_arc(     # 目盛外側円弧
        #                        60, 400, 1860, 2200,
        #                        extent = 120, start = 30, style = "arc", outline = "black",
        #                        width = 5, tag = "b_high")
        self.canvas.create_arc(     # 目盛内側円弧
                                160, 500, 1760, 2100,
                                extent = 120, start = 30, style = "arc", outline = "black",
                                width = 5, tag = "b_high")
        for i in range(30,151,40):  # 目盛特大
            self.canvas.create_line(960+(960*cos(pi/180*i)), 1300-(960*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 12,
                                    tag = "b_high")
        for i in range(30,151,20):  # 目盛大
            self.canvas.create_line(960+(940*cos(pi/180*i)), 1300-(940*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 9,
                                    tag = "b_high")
        for i in range(30,151,4):  # 目盛中
            self.canvas.create_line(960+(920*cos(pi/180*i)), 1300-(920*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 6,
                                    tag = "b_high")
        for i in range(30,151,2):  # 目盛小
            self.canvas.create_line(960+(900*cos(pi/180*i)), 1300-(900*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 3,
                                    tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*150)),
                                1300-(self.meter_fontpos*sin(pi/180*150)),
                                text = "0", font = ("", self.meter_fontsize ),
                                tag = "b_high")
        #self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*145)),
        #                        1300-(self.meter_fontpos*sin(pi/180*145)),
        #                        text = "100", font = ("", self.meter_fontsize),
        #                        tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*130)),
                                1300-(self.meter_fontpos*sin(pi/180*130)),
                                text = "500", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*110)),
                                1300-(self.meter_fontpos*sin(pi/180*110)),
                                text = "1000", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*90)),
                                1300-(self.meter_fontpos*sin(pi/180*90)),
                                text = "1500", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*70)),
                                1300-(self.meter_fontpos*sin(pi/180*70)),
                                text = "2000", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*50)),
                                1300-(self.meter_fontpos*sin(pi/180*50)),
                                text = "2500", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(960+((self.meter_fontpos-40)*cos(pi/180*30)),
                                1300-((self.meter_fontpos+40)*sin(pi/180*30)),
                                text = "3000", font = ("", self.meter_fontsize),
                                tag = "b_high")
        self.canvas.create_text(870, 880,
                                text = "daN", font = ('', 64),
                                tag = "b_high")
        self.canvas.create_text(1200, 880,
                                text = "daN", font = ('', 64),
                                tag = "b_high")
        self.canvas.tag_lower("b_high")

    def s_scale(self):
        self.canvas.delete("a_scale")
        self.canvas.delete("b_low")
        self.canvas.delete("b_high")
        self.label1.set("SPEEDOMETER")
        self.canvas.create_arc(60, 400, 1860, 2200,
                                    extent = 120, start = 30, style = "arc", outline = "black",
                                    width = 3, tag = "s_scale")
        self.canvas.create_arc(160, 500, 1760, 2100,
                                    extent = 120, start = 30, style = "arc", outline = "black",
                                    width = 3, tag = "s_scale")
        self.canvas.create_arc(200, 540, 1720, 2060,
                                    extent = 120, start = 30, style = "arc", outline = "red",
                                    width = 40, tag = "s_scale")
        self.canvas.create_arc(200, 540, 1720, 2060,
                                    extent = 11.5, start = 107.5, style = "arc", outline = "lime",
                                    width = 40, tag = "s_scale")
        for i in range(30,151,1):   # 目盛小
            self.canvas.create_line(960+(900*cos(pi/180*i)), 1300-(900*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 3,
                                    tag = "s_scale")
        for i in range(30,151,5):   # 目盛中
            self.canvas.create_line(960+(920*cos(pi/180*i)), 1300-(920*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 6,
                                    tag = "s_scale")
        for i in range(30,151,10):  # 目盛大
            self.canvas.create_line(960+(950*cos(pi/180*i)), 1300-(950*sin(pi/180*i)),
                                    960+(800*cos(pi/180*i)), 1300-(800*sin(pi/180*i)),
                                    fill = "black", width = 12,
                                    tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*150)),
                                1300-(self.meter_fontpos*sin(pi/180*150)),
                                text = "0", font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*130)),
                                1300-(self.meter_fontpos*sin(pi/180*130)),
                                text = "20",font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*110)),
                                1300-(self.meter_fontpos*sin(pi/180*110)),
                                text = "40", font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*90)),
                                1300-(self.meter_fontpos*sin(pi/180*90)),
                                text = "60", font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*70)),
                                1300-(self.meter_fontpos*sin(pi/180*70)),
                                text = "80", font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+(self.meter_fontpos*cos(pi/180*50)),
                                1300-(self.meter_fontpos*sin(pi/180*50)),
                                text = "100", font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(960+((self.meter_fontpos-30)*cos(pi/180*30)),
                                1300-(self.meter_fontpos*sin(pi/180*30)),
                                text = "120",font = ("", self.meter_fontsize),
                                tag = "s_scale")
        self.canvas.create_text(1100, 800,
                                text = 'km/h', font = ('', self.meter_fontsize),
                                tag = "s_scale") # 単位表示
        self.canvas.tag_lower("s_scale")

    def updateMeterLine0(self, a):
        """Draw a meter line"""
        self.angle0 = a
        x = 960 - 900 * cos(a * pi)
        y = 1300 - 900 * sin(a * pi)
        self.canvas.coords(self.meter0, 960, 1300, x, y)
        var = float(self.var0.get())/10
        if var > 0:
            self.a_sign.set("IN")
        elif var < 0:
            self.a_sign.set("OUT")
        else:
            self.a_sign.set("")
        var_fabs = fabs(var)
        self.a_data.set(var_fabs)

    def updateMeterLine1(self, a):
        """Draw a meter line"""
        self.angle1 = a
        x = 960 - 900 * cos(a * pi)
        y = 1300 - 900 * sin(a * pi)
        self.canvas.coords(self.meter1, 960, 1300, x, y)
        var = self.var1.get()
        self.bl_data.set(var)

    def updateMeterLine2(self, a):
        """Draw a meter line"""
        self.angle2 = a
        x = 960 - 900 * cos(a * pi)
        y = 1300 - 900 * sin(a * pi)
        self.canvas.coords(self.meter2, 960, 1300, x, y)
        var = self.var2.get()
        self.br_data.set(var)

    def updateMeterLine3(self, a):
        """Draw a meter line"""
        self.angle3 = a
        x = 960 - 900 * cos(a * pi)
        y = 1300 - 900 * sin(a * pi)
        self.canvas.coords(self.meter3, 960, 1300, x, y)
        var = float(self.var3.get())/10
        self.s_data.set(var)

    def updateMeter(self, name1, name2, op):
        """Convert variable to angle on trace"""
        var0 = self.var0.get()
        var1 = self.var1.get()
        var2 = self.var2.get()
        var3 = self.var3.get()
        if self.panel == 1:
            if var1 < 1200 and var2 < 1200 and self.angle_b == 0:
                mini = 0
                maxi = 1200
            elif var1 < 1100 and var2 < 1100 and self.angle_b == 1:
                mini = 0
                maxi = 1200
                self.angle_b = 0
            else:
                mini = 0
                maxi = 3000
                self.angle_b = 1
            if self.angle_b == 1 and self.b_type == 0 :
                self.b_high_range()
            if self.angle_b == 0 and self.b_type == 1 :
                self.b_low_range()
            pos1 = (var1 - mini) / (maxi - mini)
            pos2 = (var2 - mini) / (maxi - mini)
            self.updateMeterLine1(pos1 * (0.2*120/36) + (0.2*30/36))
            self.updateMeterLine2(pos2 * (0.2*120/36) + (0.2*30/36))
        elif self.panel == 2:
            mini = 0
            maxi = 1200
            pos = (var3 - mini) / (maxi - mini)
            self.updateMeterLine3(pos * (0.2*120/36) + (0.2*30/36))
        else:
            mini = -150
            maxi = 150
            pos = (var0 - mini) / (maxi - mini)
            self.updateMeterLine0(pos * (0.2*90/36) + (0.2*45/36))


if __name__ == '__main__':
        root = tk.Tk()              # メインウインドウの生成
        root.resizable(0, 0)        # ウィンドウのサイズ固定設定 0:固定/1:自由
        root.geometry("1920x1080")   # 起動時のウィンドウのサイズ
        root.overrideredirect(True) # タイトルバー及び枠を消す
        root.config(bg="grey55")    # ウインドウ背景色
        meter = Meter(root)
        meter.pack()

        quit = tk.Button(root)  # 終了ボタンウィジェットの定義
        quit["text"] = "QUIT"
        quit["fg"] = "red"
        quit["command"] = root.destroy
        quit.place(x = 1860, y = 20)

        root.mainloop()

