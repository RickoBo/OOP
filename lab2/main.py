from tkinter import Tk
from app import App, EditorConfig
from editors.point_editor import PointEditor
from editors.line_editor import LineEditor
from editors.rectangle_editor import RectangleEditor
from editors.ellipse_editor import EllipseEditor
from repositories.static_repository import StaticRepository

CONFIG = {
  'window_size': '800x600',
  'title': 'Lab 2',
  'repository_capacity': 101,
  'editors': {
    'point': {
      'radius': 2,
      'fill': 'black' 
    },
    'line': {
      "fill": "black",
      'rubber_fill': 'red'
    },
    'rectangle': {
      'outline': 'black',
      'fill': 'lightgreen',
      'rubber_outline': 'red',
      'rubber_fill': ''
    },
    'ellipse': {
      'outline': 'black',
      'fill': 'white',
      'rubber_outline': 'red',
      'rubber_fill': ''
    }
  }
}

if __name__ == '__main__':
  root = Tk()
  root.geometry(CONFIG['window_size'])
  root.title(CONFIG['title'])

  repository = StaticRepository(CONFIG['repository_capacity'])
  editor_configs = {
    'point': EditorConfig(
      label='Point',
      editor_cls=PointEditor,
      options=CONFIG['editors']['point']
    ),
    'line': EditorConfig(
      label='Line',
      editor_cls=LineEditor,
      options=CONFIG['editors']['line']
    ),
    'rectangle': EditorConfig(
      label='Rectangle',
      editor_cls=RectangleEditor,
      options=CONFIG['editors']['rectangle']
    ),
    'ellipse': EditorConfig(
      label='Ellipse',
      editor_cls=EllipseEditor,
      options=CONFIG['editors']['ellipse']
    )
  } 
  
  app = App(root, repository, editor_configs)
  app.run()