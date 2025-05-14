# 展示 Button 的使用
import tkinter as tk
from functools import partial

def say_hello(name):
    label['text'] = f"Hello world count: {name}"

def on_enter(event):
    hover_label['text'] = "Mouse enter"

def on_leave(event):
    hover_label['text'] = "Mouse leave"

window = tk.Tk()
window.title('Button example')
window.geometry('500x500')

label = tk.Label(window)
hover_label = tk.Label(window)

button = tk.Button(window, text='Hello 按鈕', command=partial(say_hello, "Alice"))

hover_button = tk.Button(window, text="懸停效果")
hover_button.bind("<Enter>", on_enter)
hover_button.bind("<Leave>", on_leave)

button.pack()
label.pack()
hover_button.pack()
hover_label.pack()

resultsContents = tk.StringVar()
var_label = tk.Label(window, textvariable=resultsContents)
resultsContents.set('New value to display')

var_label.pack()

window.mainloop()
