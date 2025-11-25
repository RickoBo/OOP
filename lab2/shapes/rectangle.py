from tkinter import Canvas
from shapes.shape import Shape

class Ractangle(Shape):
  def __init__(self, x1: float, y1: float, x2: float, y2: float, fill: str, outline: str) -> None:
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.fill = fill
    self.outline = outline

  def draw(self, canvas: Canvas) -> None:
    self._id = canvas.create_rectangle(
      self.x1,
      self.y1,
      self.x2,
      self.y2,
      fill=self.fill,
      outline=self.outline
    )

  def erase(self, canvas: Canvas) -> None:
    canvas.delete(self._id)
    