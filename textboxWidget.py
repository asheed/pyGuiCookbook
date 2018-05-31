#!/usr/bin/env python
# -*- coding: utf8 -*

import tkinter as tk
from tkinter import ttk

win = tk.Tk()               # Tk 객체 생성
win.title("TextBox Widget")     # 창 제목 설정
# win.geometry("200x200")
# 라벨 추가
# ttk.Label(win, text="A Label").grid(column=0, row=0)    # grid layout manager 사용
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button & click event
def clickMe():
	if name.get() == '':
		action.configure(text='안녕! 무명씨!' + ' ' + numberChosen.get())
	else:
		action.configure(text='안녕! ' + name.get() + ' ' + numberChosen.get())

# 라벨 변경
ttk.Label(win, text="이름을 입력하세요:").grid(column=0, row=0)

# textbox 추가
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()
# add Button
action = ttk.Button(win, text="눌러요!", command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled')

ttk.Label(win, text="숫자를 선택하세요:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

#======================
# Start GUI
#======================
win.mainloop()              # 실행
