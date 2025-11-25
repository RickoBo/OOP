from repositories.repository import Repository
from shapes.shape import Shape

class StaticRepository(Repository):
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.shapes = []
  
  def add(self, shape: Shape):
    if self.can_add():
      self.shapes.append(shape)
      print(f"Shape added. Total shapes: {len(self.shapes)} / {self.capacity}")

  def remove_all(self):
    self.shapes.clear()

  def can_add(self):
    return len(self.shapes) < self.capacity
    
    
    