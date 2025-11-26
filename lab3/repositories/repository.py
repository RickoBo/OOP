from abc import ABC, abstractmethod
from shapes.shape import Shape

class Repository(ABC):
  @abstractmethod
  def add(self, shape: Shape) -> None:
    pass

  @abstractmethod
  def remove_all(self) -> None:
    pass

  @abstractmethod
  def can_add(self) -> bool:
    pass