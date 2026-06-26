from datetime import datetime
from .item import Item

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .storage import Storage


class Node:
    def __init__(self, name: str, description: str, picture: str, parent: Node | Storage) -> None:
        self.name = name
        self.description = description
        self.picture = picture
        self.parent = parent
        self.children: list[Node | Item] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return f"Storage: {self.name}, {self.description}, {self.picture}, {self.created_at}, {self.updated_at}"

    def add_child(self, child: Node | Item) -> None:
        self.children.append(child)
