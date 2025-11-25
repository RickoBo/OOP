import tkinter as tk
from module_b1 import TextDialog
from module_b2 import SliderDialog

def handle_work1():
    dialog = TextDialog(root)
    root.wait_window(dialog)
    result = dialog.result
    
    if result is not None:
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="(Action canceled)")

def handle_work2():
    dialog = SliderDialog(root)
    root.wait_window(dialog)
    result = dialog.result
    
    if result is not None:
        result_label.config(text=f"Enter a number: {result}")
    else:
        result_label.config(text="(Action canlceled)")

root = tk.Tk()
root.title("Lab 1")
root.geometry("450x300")

result_label = tk.Label(root, text="Pick a task in a navbar", font=("Arial", 14))
result_label.pack(expand=True)

menubar = tk.Menu(root)
root.config(menu=menubar)

work_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tasks", menu=work_menu)

work_menu.add_command(label="Task 1", command=handle_work1)
work_menu.add_command(label="Task 2", command=handle_work2)

root.mainloop()