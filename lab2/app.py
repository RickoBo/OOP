from dataclasses import dataclass
import tkinter as tk
from typing import Type
from editors.editor import Editor
from repositories.repository import Repository

@dataclass
class EditorConfig:
  label: str
  editor_cls: Type[Editor]
  options: dict

  def __init__ (self, label: str, editor_cls: Type[Editor], options: dict = {}):
    self.label = label
    self.editor_cls = editor_cls
    self.options = options


class App:
  def __init__(self, root: tk.Tk, repository: Repository, editor_configs: dict[str, EditorConfig]):
    self.root = root
    self.repository = repository
    self.editor_configs = editor_configs

    self.current_editor: Editor | None = None

    self.create_menu()

    self.canvas = tk.Canvas(self.root, bg='white', borderwidth=0)
    self.canvas.pack(fill=tk.BOTH, expand=True)

    self.canvas.bind('<ButtonPress-1>', self.on_press)
    self.canvas.bind('<ButtonRelease-1>', self.on_release)
    self.canvas.bind('<B1-Motion>', self.on_drag)

  def run(self):
    self.root.mainloop()

  def create_menu(self):
    menubar = tk.Menu(self.root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label='Clear All', command=self.clear_all)
    file_menu.add_command(label='Exit', command=self.root.quit)
    menubar.add_cascade(label='File', menu=file_menu)

    shape_menu = tk.Menu(menubar, tearoff=0)

    for name, config in self.editor_configs.items():
      shape_menu.add_radiobutton(
        label=config.label,
        value=name,
        command=lambda cfg=config: self.select_editor(
          cfg.editor_cls(self.canvas, **cfg.options),
          cfg.label
        )
      )
    menubar.add_cascade(label='Shapes', menu=shape_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label='About', command=self.show_about)
    menubar.add_cascade(label='Help', menu=help_menu)

    self.root.config(menu=menubar)

  def select_editor(self, editor: Editor, name: str):
    self.current_editor = editor
    self.root.title(f'Lab 2 - {name}')

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

  def show_about(self):
    tk.messagebox.showinfo(
      'About',
      'Lab 2\n\n'
      'A simple drawing application.\n'
      'Created as part of the Software Engineering course.'
    )