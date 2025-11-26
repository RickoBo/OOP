from tkinter import Canvas
from shapes.shape import Shape

class Point(Shape):
  def __init__(self, x: float, y: float, radius: float, fill: str) -> None:
    self.x = x
    self.y = y
    self.radius = radius
    self.fill = fill

  def draw(self, canvas: Canvas) -> None:
    self._id = canvas.create_oval(
      self.x - self.radius,
      self.y - self.radius,
      self.x + self.radius,
      self.y + self.radius,
      fill=self.fill
    )

  def erase(self, canvas: Canvas) -> None:
    canvas.delete(self._id)
    