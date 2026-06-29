from models.root import Root
from models.node import Node, NodeType
from pathlib import Path


def main():
    root = Root()
    node1 = Node("Hello", None, None, NodeType.Storage)
    node2 = Node("World", None, None, NodeType.Storage)
    node3 = Node("socks", None, None, NodeType.Item)
    root.create_node(Path("/"), node1)
    root.create_node(Path("/Hello"), node2)
    root.create_node(Path("/Hello/World"), node3)
    print(root.serialize_path(2))
    print(node3.get_path())

if __name__ == "__main__":
    main()
