import tkinter as tk


class TextDialog(tk.Toplevel):
    def __init__(self, parent, center_fn):
        super().__init__(parent)
        width, height = 300, 150
        self.title("Task 1")
        self.transient(parent)
        self.grab_set()
        center_fn(self, parent, width, height)

        self.result = None
        
        tk.Label(self, text="Enter any text:").pack(padx=20, pady=10)
        
        self.entry = tk.Entry(self, width=40)
        self.entry.pack(padx=20, pady=5)
        
        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=15)

        ok_button = tk.Button(button_frame, text="Yes", width=10, command=self._on_ok)
        ok_button.pack(side=tk.LEFT, padx=10)
        
        cancel_button = tk.Button(button_frame, text="Cancel", width=10, command=self._on_cancel)
        cancel_button.pack(side=tk.LEFT, padx=10)

        self.protocol("WM_DELETE_WINDOW", self._on_cancel)

    def _on_ok(self):
        self.result = self.entry.get()
        self.destroy()

    def _on_cancel(self):
        self.result = None
        self.destroy()