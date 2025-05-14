# 展示 CheckButton 的使用
import tkinter as tk

window = tk.Tk()
window.title('CheckButton example')
window.geometry('500x500')

# 創建 CheckButton
def on_check():
    if check_var.get():
        label['text'] = "CheckButton 被選中"
    else:
        label['text'] = "CheckButton 未被選中"

check_var = tk.IntVar()
check_button = tk.Checkbutton(window, text="選擇我", variable=check_var, command=on_check)
check_button.pack()
label = tk.Label(window, text="CheckButton 未被選中")
label.pack()

window.mainloop()
