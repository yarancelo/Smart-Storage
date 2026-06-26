from pathlib import Path
from .item import Item
from .node import Node

class Storage:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.nodes = []

    def store(self, node: Node | Item, path: Path) -> None:
        for parent in reversed(path.parents):
