# 展示 Entry 輸入框的使用
import tkinter as tk

window = tk.Tk()
window.title('Entry example')
window.geometry('500x500')

# 創建基本輸入框
label = tk.Label(window, text="基本輸入框")
label.pack()
entry = tk.Entry(window)
entry.insert(0, "預設文字")
entry.pack()

# 創建密碼輸入框
password_label = tk.Label(window, text="密碼輸入框")
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# 建立唯讀輸入框
readonly_label = tk.Label(window, text="唯讀輸入框")
readonly_label.pack()
readonly_string_var = tk.StringVar()
readonly_string_var.set("這是唯讀輸入框")
readonly_entry = tk.Entry(window, textvariable=readonly_string_var, state='readonly')
readonly_entry.pack()

# 事件綁定：按下 Enter、取得焦點、失去焦點
event_label = tk.Label(window, text="目前尚未執行事件")
event_label.pack()

def handle_on_enter(event):
    event_label['text'] = f"輸入框事件: 按下 Enter 鍵，內容：{event.widget.get()}"

def handle_on_focus_in(event):
    event_label['text'] = "輸入框事件: 獲得焦點"

def handle_on_focus_out(event):
    event_label['text'] = "輸入框事件: 失去焦點"

def handle_on_change(var, index, mode):
    event_label['text'] = f"輸入框內容監測到變化：{event_string_var.get()}"

event_string_var = tk.StringVar()
event_string_var.trace_add("write", handle_on_change)
event_entry = tk.Entry(window, textvariable=event_string_var)
event_entry.bind("<Return>", handle_on_enter)
event_entry.bind("<FocusIn>", handle_on_focus_in)
event_entry.bind("<FocusOut>", handle_on_focus_out)
event_entry.pack()

window.mainloop()
