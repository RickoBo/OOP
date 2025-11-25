from tkinter import Canvas, Event
from editors.editor import Editor
from shapes.shape import Shape
from shapes.ellipse import Ellipse

class EllipseEditor(Editor):
  def __init__(self, canvas: Canvas, fill: str, rubber_fill: str, outline: str, rubber_outline: str) -> None:
    self.canvas = canvas
    self.fill = fill
    self.outline = outline
    self.rubber_outline = rubber_outline
    self.rubber_fill = rubber_fill
    self.start_point = None
    self.temp_ellipse = None
    
  def on_press(self, event: Event) -> None:
    self.start_point = {
      'x': event.x,
      'y': event.y
    }
    
  def on_release(self, event: Event) -> Shape:
    if self.start_point is None:
      return
    
    if self.temp_ellipse:
      self.temp_ellipse.erase(canvas=self.canvas)

    ellipse = Ellipse(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.fill,
      outline=self.outline
    )
    
    ellipse.draw(canvas=self.canvas)
    self.temp_ellipse = None
    self.start_point = None
    return ellipse

  def on_drag(self, event: Event) -> None:
    if self.start_point is None:
      return
    
    if self.temp_ellipse:
      self.temp_ellipse.erase(canvas=self.canvas)
    
    self.temp_ellipse = Ellipse(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.rubber_fill,
      outline=self.rubber_outline
    )
    
    self.temp_ellipse.draw(canvas=self.canvas)