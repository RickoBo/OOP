from abc import ABC, abstractmethod
from tkinter import Canvas


class Shape(ABC):
  @abstractmethod
  def draw(self, canvas: Canvas) -> None:
    pass

  @abstractmethod
  def erase(self, canvas: Canvas) -> None:
    pass
