#!/usr/bin/env python
# -*- coding: utf8 -*

# imports
import tkinter as tk
from tkinter import ttk

win = tk.Tk()               # Tk 객체 생성
win.title("Python GUI")     # 창 제목 설정
# win.geometry("200x200")
# 라벨 추가
# ttk.Label(win, text="A Label").grid(column=0, row=0)    # grid layout manager 사용
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button & click event
def clickMe():
	action.configure(text="** I have been Clicked! **")
	aLabel.configure(foreground='red')

# add Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()              # 실행
