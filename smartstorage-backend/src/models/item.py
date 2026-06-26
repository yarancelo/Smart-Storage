from datetime import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .node import Node

class Item:
    def __init__(self, name: str, description: str, quantity: int, picture: str, parent: "Node") -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.picture = picture
        self.parent = parent
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return f"Item: {self.name}, {self.description}, {self.quantity}, {self.picture}, {self.created_at}, {self.updated_at}"