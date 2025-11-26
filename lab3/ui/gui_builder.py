import tkinter as tk
from tkinter import messagebox
from configs.editor_config import EditorConfig
from ui.toolbar.tooblar_icon import ToolbarIcon

class GUIBuilder:
  def __init__(self, root: tk.Tk):
      self.root = root
      self.canvas: tk.Canvas | None = None
      self.toolbar_icons: list[ToolbarIcon] = []

  def setup_canvas(self) -> tk.Canvas:
      self.canvas = tk.Canvas(self.root, bg='white', borderwidth=0)
      self.canvas.pack(fill=tk.BOTH, expand=True)
      return self.canvas

  def setup_toolbar(self, editor_configs: dict[str, EditorConfig], icons_path: dict[str, str], on_select_callback: callable):
      toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
      toolbar.pack(side=tk.TOP, fill=tk.X)

      for name, config in editor_configs.items():
          icon_path = icons_path.get(name, '')
          if icon_path:
              cmd = lambda cfg=config: on_select_callback(cfg.editor_cls, cfg.label, cfg.options)

              button = ToolbarIcon(
                  icon_path=icon_path,
                  toolbar=toolbar,
                  tooltip=config.label,
                  value=name,
                  command=cmd
              )
              button.render()
              self.toolbar_icons.append(button)

  def setup_menu(self, editor_configs: dict[str, EditorConfig], callbacks: dict):
      menubar = tk.Menu(self.root)

      file_menu = tk.Menu(menubar, tearoff=0)
      file_menu.add_command(label='Clear All', command=callbacks.get('clear'))
      file_menu.add_command(label='Exit', command=callbacks.get('exit'))
      menubar.add_cascade(label='File', menu=file_menu)

      shape_menu = tk.Menu(menubar, tearoff=0)
      on_select = callbacks.get('select_editor')
      
      for name, config in editor_configs.items():
          cmd = lambda cfg=config: on_select(cfg.editor_cls, cfg.label, cfg.options)
          
          shape_menu.add_radiobutton(
              label=config.label,
              value=name,
              command=cmd
          )
      menubar.add_cascade(label='Shapes', menu=shape_menu)

      help_menu = tk.Menu(menubar, tearoff=0)
      help_menu.add_command(label='About', command=self.show_about)
      menubar.add_cascade(label='Help', menu=help_menu)

      self.root.config(menu=menubar)

  def set_title(self, title: str):
      self.root.title(title)

  def show_about(self):
      messagebox.showinfo(
          'About',
          'Lab 3\n\n'
          'A simple drawing application.\n'
          'Created as part of the Software Engineering course.'
      )