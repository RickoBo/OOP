from tkinter import Frame, PhotoImage, Radiobutton, LEFT 
from idlelib.tooltip import Hovertip


class ToolbarIcon:
  def __init__(self, icon_path: str, toolbar: Frame, tooltip: str, value: str, command: callable):
    self.icon = PhotoImage(file=icon_path)
    self.button = Radiobutton(
      toolbar, 
      image=self.icon, 
      indicatoron=0, 
      value=value, 
      command=command, 
      padx=5, 
      pady=5
      )
    self.tooltip = tooltip
    
    
  def render(self):
    self.button.pack(side=LEFT, padx=2, pady=2)
    Hovertip(self.button, self.tooltip, hover_delay=500)