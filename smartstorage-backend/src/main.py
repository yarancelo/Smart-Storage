from models.root import Root
from models.node import Node, NodeType
from pathlib import Path


def main():
    root = Root()
    node1 = Node("Hello", None, None, NodeType.Storage)
    node2 = Node("World", None, None, NodeType.Storage)
    root.create_node(Path("/"), node1)
    root.create_node(Path("/Hello"), node2)
    print(root.serialize_path(2))

if __name__ == "__main__":
    main()
