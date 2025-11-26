from dataclasses import dataclass
from typing import Type

from editors.editor import Editor


@dataclass
class EditorConfig:
  label: str
  editor_cls: Type[Editor]
  options: dict