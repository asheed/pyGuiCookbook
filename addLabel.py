#!/usr/bin/env python
# -*- coding: utf8 -*

# imports
import tkinter as tk
from tkinter import ttk

win = tk.Tk()               # Tk 객체 생성
win.title("Python GUI")     # 창 제목 설정
win.geometry("200x200")
# 라벨 추가
ttk.Label(win, text="A Label").grid(column=0, row=0)    # grid layout manager 사용
win.mainloop()              # 실행
