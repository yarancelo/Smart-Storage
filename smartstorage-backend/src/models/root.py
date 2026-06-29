from pathlib import Path
from exc import NodeIsAItemError, NodeAlreadyExistsError, NodeDoesNotExistError

from .node import Node, NodeType

class Root:
    def __init__(self) -> None:
        self.nodes: list [Node] = []

    def create_node(self, path: Path, new_node: Node) -> None:
        if new_node.type == NodeType.Item:
            raise NodeIsAItemError

        path_list: list[str] = list(path.parts[1:])
        if len(path_list) == 0:
            found = next((node for node in self.nodes if node.name == new_node.name), None)
            if found is not None:
                raise NodeAlreadyExistsError
            else:
                self.nodes.append(new_node)
        else:
            found = next((node for node in self.nodes if node.name == path_list[0]), None)
            if found is None:
                raise NodeDoesNotExistError
            found.create_new_node(path_list[1:], new_node)

    def serialize_path(self, indent: int) -> str:
        paths: list[str] = [f"/\n"]
        for node in self.nodes:
            paths.append(node.serialize_path(indent, 1))

        return "".join(paths)