# 展示下拉式選單的使用
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('ComboBox example')
window.geometry('500x500')

# 創建 ComboBox
label = tk.Label(window, text="下拉式選單")
label.pack()

options = ["台北", "台中", "高雄", "花蓮"]
combo_box = ttk.Combobox(window, values=options)
combo_box.current(0)  # 預設選擇第一個選項
combo_box.pack()

window.mainloop()
