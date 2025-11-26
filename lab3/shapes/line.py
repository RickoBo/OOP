from tkinter import Canvas
from shapes.shape import Shape

class Line(Shape):
  def __init__(self, x1: float, y1: float, x2: float, y2: float, fill: str) -> None:
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    self.fill = fill

  def draw(self, canvas: Canvas) -> None:
    self._id = canvas.create_line(
      self.x1,
      self.y1,
      self.x2,
      self.y2,
      fill=self.fill
    )

  def erase(self, canvas: Canvas) -> None:
    canvas.delete(self._id)
    