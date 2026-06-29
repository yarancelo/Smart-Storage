from datetime import datetime
from enum import Enum
from exc import NodeDoesNotExistError, NodeAlreadyExistsError
from uuid import UUID, uuid7


class NodeType(Enum):
    Storage = 1
    Item = 2


class Node:
    def __init__(self,
        name: str,
        description: str | None,
        picture: str | None,
        node_type: NodeType
    ) -> None:
        self.name = name
        self.description = description
        self.picture = picture
        self.type = node_type
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.parent: Node | None = None
        self.uuid: UUID = uuid7()

        if node_type == NodeType.Storage:
            self.children: list[Node] = []

    def __repr__(self) -> str:
        return f"Storage: {self.name}, {self.description}, {self.picture}, {self.created_at}, {self.updated_at}"

    def create_new_node(self, path: list[str], new_node: Node) -> None:
        if len(path) == 0:
            found: Node | None = next((node for node in self.children if node.name == new_node.name), None)
            if found is not None:
                raise NodeAlreadyExistsError("/".join(path), new_node, "Node already exists in this directory")

            self.children.append(new_node)
            new_node.set_parent(self)
            return
        else:
            found: Node | None = next((node for node in self.children if node.name == path[0]), None)
            if found is None:
                raise NodeDoesNotExistError("/".join(path), new_node, "Node does not exist")

            found.create_new_node(path[1:], new_node)

    def delete_node(self, path: list[str]) -> None:
        if len(path) == 0:



    def set_parent(self, parent: Node):
        self.parent = parent

    def serialize_path(self, indent: int, level: int) -> str:
        paths: list[str] = [f"{indent * level * ' '}{self.name}/\n"]
        if self.type == NodeType.Storage:
            for child in self.children:
                paths.append(child.serialize_path(indent, level + 1))

            return "".join(paths)
        else:
            return f"{indent * level * ' '}{self.name}\n"

    def get_path(self) -> str:
        if self.parent is None:
            return f"/{self.name}"

        if self.parent is None:
            return self.name

        return f"{self.parent.get_path()}/{self.name}"