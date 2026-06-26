from pathlib import Path

from .protocols import CombinedNodeProtocols


class Root:
    def __init__(self) -> None:
        self.nodes: list [CombinedNodeProtocols] = []

    def create_node(self, path: Path, node: CombinedNodeProtocols) -> None:
        for index, part in enumerate(path.parts):
            is_last: bool = (index == len(path.parts) - 1)

            if is_last:
                self.nodes.append(node)
                return

    def serialize_path(self, indent: int) -> str:
        paths: list[str] = [f"/\n"]
        for node in self.nodes:
            paths.append(node.serialize_path(indent, 1))

        return "".join(paths)