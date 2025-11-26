from abc import ABC, abstractmethod
from tkinter import Event
from shapes.shape import Shape

class Editor(ABC):
  @abstractmethod
  def on_press(self, event: Event) -> None:
    pass

  @abstractmethod
  def on_release(self, event: Event) -> Shape:
    pass

  @abstractmethod
  def on_drag(self, event: Event) -> None:
    pass