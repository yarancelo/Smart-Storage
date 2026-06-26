from datetime import datetime
from .item import Item
from pathlib import Path

class Node:
    def __init__(self, name: str, description: str | None, picture: str | None, parent: Node | None) -> None:
        self.name = name
        self.description = description
        self.picture = picture
        self.parent = parent
        self.children: list[Node | Item] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return f"Storage: {self.name}, {self.description}, {self.picture}, {self.created_at}, {self.updated_at}"

    def create_storage_node(self, path: Path, node: Node | Item) -> str:
        ...

    def serialize_path(self, indent: int, level: int) -> str:
        paths: list[str] = [f"{indent * level * ' '}{self.name}/\n"]
        for child in self.children:
            paths.append(child.serialize_path(indent, level + 1))

        return "".join(paths)