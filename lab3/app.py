import tkinter as tk
from typing import Type
from configs.editor_config import EditorConfig
from editors.editor import Editor
from repositories.repository import Repository
from ui.gui_builder import GUIBuilder

class App:
  def __init__(self, root: tk.Tk, repository: Repository, editor_configs: dict[str, EditorConfig], icons_path: dict[str, str]):
      self.repository = repository
      self.editor_configs = editor_configs
      self.current_editor: Editor | None = None
    
      self.gui = GUIBuilder(root)
      
      self.gui.setup_toolbar(
          editor_configs=self.editor_configs,
          icons_path=icons_path,
          on_select_callback=self.switch_editor
      )

      menu_callbacks = {
          'clear': self.clear_all,
          'exit': root.quit,
          'select_editor': self.switch_editor
      }
      self.gui.setup_menu(self.editor_configs, menu_callbacks)
      self.canvas = self.gui.setup_canvas()

      self.canvas.bind('<ButtonPress-1>', self.on_press)
      self.canvas.bind('<ButtonRelease-1>', self.on_release)
      self.canvas.bind('<B1-Motion>', self.on_drag)

  def run(self):
      self.gui.root.mainloop()

  def switch_editor(self, editor_cls: Type[Editor], label: str, options: dict):
      self.current_editor = editor_cls(self.canvas, **options)
      self.gui.set_title(f'Lab 2 - {label}')

  def clear_all(self):
      self.canvas.delete('all')
      self.repository.remove_all()
  
  def on_press(self, event: tk.Event):
      if self.repository.can_add() and self.current_editor:
          self.current_editor.on_press(event)
  
  def on_release(self, event: tk.Event):
      if self.current_editor:
          shape = self.current_editor.on_release(event)
          self.repository.add(shape)

  def on_drag(self, event: tk.Event):
      if self.current_editor:
          self.current_editor.on_drag(event)