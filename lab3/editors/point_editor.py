from tkinter import Canvas, Event
from editors.editor import Editor
from shapes.shape import Shape
from shapes.point import Point

class PointEditor(Editor):
  def __init__(self, canvas: Canvas, radius: float, fill: str) -> None:
    self.canvas = canvas
    self.radius = radius
    self.fill = fill

  def on_press(self, event: Event) -> None:
    self.point = Point(
      x=event.x, 
      y=event.y, 
      radius=self.radius, 
      fill=self.fill
    )
    self.point.draw(canvas=self.canvas)
 
  def on_release(self, event: Event) -> Shape:
    return self.point
  
  def on_drag(self, event: Event) -> None:
    pass