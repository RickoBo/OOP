from tkinter import Canvas, Event
from editors.editor import Editor
from shapes.shape import Shape
from shapes.line import Line

class LineEditor(Editor):
  def __init__(self, canvas: Canvas, fill: str, rubber_fill: str) -> None:
    self.canvas = canvas
    self.fill = fill
    self.rubber_fill = rubber_fill
    self.start_point = None
    self.temp_line = None
    
  def on_press(self, event: Event) -> None:
    self.start_point = {
      'x': event.x,
      'y': event.y
    }
    
  def on_release(self, event: Event) -> Shape:
    if self.start_point is None:
      return
    
    if self.temp_line:
      self.temp_line.erase(canvas=self.canvas)

    line = Line(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.fill
    )
    
    line.draw(canvas=self.canvas)
    self.temp_line = None
    self.start_point = None
    return line

  def on_drag(self, event: Event) -> None:
    if self.start_point is None:
      return
    
    if self.temp_line:
      self.temp_line.erase(canvas=self.canvas)
    
    self.temp_line = Line(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.rubber_fill
    )
    
    self.temp_line.draw(canvas=self.canvas)