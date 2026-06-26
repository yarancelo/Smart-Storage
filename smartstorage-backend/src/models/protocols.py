from typing import Protocol
from pathlib import Path

from .item import Item
from .node import Node

class SerializablePath(Protocol):
    def serialize_path(self, indent: int, level: int) -> str:
        ...

class ChildStorageNodeCreatable(Protocol):
    def create_storage_node(self, path: Path, node: Node | Item) -> str:
        ...

class CombinedNodeProtocols(SerializablePath, ChildStorageNodeCreatable):
    ...