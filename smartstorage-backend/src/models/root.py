from pathlib import Path
from exc import NodeIsAItemError, NodeAlreadyExistsError, NodeDoesNotExistError

from .node import Node, NodeType

class Root:
    def __init__(self) -> None:
        self.nodes: list [Node] = []

    def create_node(self, path: Path, new_node: Node) -> None:
        path_list: list[str] = list(path.parts[1:])
        if len(path_list) == 0:
            if new_node.type == NodeType.Item:
                raise NodeIsAItemError("/".join(path_list), new_node, "Cannot create an item in root")

            found = next((node for node in self.nodes if node.name == new_node.name), None)
            if found is not None:
                raise NodeAlreadyExistsError("/".join(path_list), new_node, "Node already exists")
            else:
                self.nodes.append(new_node)
        else:
            found = next((node for node in self.nodes if node.name == path_list[0]), None)
            if found is None:
                raise NodeDoesNotExistError("/".join(path_list), new_node, "Path does not exist")
            found.create_new_node(path_list[1:], new_node)

    def serialize_path(self, indent: int) -> str:
        paths: list[str] = [f"/\n"]
        for node in self.nodes:
            paths.append(node.serialize_path(indent, 1))

        return "".join(paths)