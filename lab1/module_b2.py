import tkinter as tk


class SliderDialog(tk.Toplevel):
    def __init__(self, parent, center_fn):
        super().__init__(parent)
        width, height = 350, 200
        self.title("Task 2")
        self.transient(parent)
        self.grab_set()
        center_fn(self, parent, width, height)

        self.result = None
        self.slider_var = tk.IntVar(value=50)

        self.value_label = tk.Label(self, text=f"Chosen number: {self.slider_var.get()}", font=("Arial", 12))
        self.value_label.pack(padx=20, pady=15)

        slider = tk.Scale(
            self,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            length=300,
            variable=self.slider_var,
            command=self._update_label
        )
        slider.pack(padx=20, pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=15)

        ok_button = tk.Button(button_frame, text="Yes", width=10, command=self._on_ok)
        ok_button.pack(side=tk.LEFT, padx=10)
        
        cancel_button = tk.Button(button_frame, text="Cancel", width=10, command=self._on_cancel)
        cancel_button.pack(side=tk.LEFT, padx=10)

        self.protocol("WM_DELETE_WINDOW", self._on_cancel)

    def _update_label(self, val):
        self.value_label.config(text=f"Chosen number: {int(float(val))}")

    def _on_ok(self):
        self.result = self.slider_var.get()
        self.destroy()

    def _on_cancel(self):
        self.result = None
        self.destroy()