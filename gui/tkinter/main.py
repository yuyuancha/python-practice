import tkinter as tk

root = tk.Tk()
root.title("問卷調查")
root.geometry("300x200")

mode = tk.StringVar(value="light")  # 預設選中淺色模式

tk.Label(root, text="選擇主題模式:").pack()

tk.Radiobutton(root, text="淺色模式", variable=mode, value="light").pack(anchor="w")
tk.Radiobutton(root, text="深色模式", variable=mode, value="dark").pack(anchor="w")
tk.Radiobutton(root, text="自動模式", variable=mode, value="auto").pack(anchor="w")

root.mainloop()
