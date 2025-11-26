from tkinter import Canvas, Event
from editors.editor import Editor
from shapes.shape import Shape
from shapes.rectangle import Ractangle

class RectangleEditor(Editor):
  def __init__(self, canvas: Canvas, fill: str, rubber_fill: str, outline: str, rubber_outline: str) -> None:
    self.canvas = canvas
    self.fill = fill
    self.outline = outline
    self.rubber_outline = rubber_outline
    self.rubber_fill = rubber_fill
    self.start_point = None
    self.temp_rect = None

  def on_press(self, event: Event) -> None:
    self.start_point = {
      'x': event.x,
      'y': event.y
    }
    
  def on_release(self, event: Event) -> Shape:
    if self.start_point is None:
      return
    
    if self.temp_rect:
      self.temp_rect.erase(canvas=self.canvas)

    rectangle = Ractangle(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.fill,
      outline=self.outline
    )
    
    rectangle.draw(canvas=self.canvas)
    self.temp_rect = None
    self.start_point = None
    return rectangle

  def on_drag(self, event: Event) -> None:
    if self.start_point is None:
      return
    
    if self.temp_rect:
      self.temp_rect.erase(canvas=self.canvas)

    self.temp_rect = Ractangle(
      x1 = self.start_point['x'],
      y1 = self.start_point['y'],
      x2 = event.x,
      y2 = event.y,
      fill=self.rubber_fill,
      outline=self.rubber_outline
    )
    
    self.temp_rect.draw(canvas=self.canvas)