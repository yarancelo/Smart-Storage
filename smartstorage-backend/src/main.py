from models.root import Root
from models.node import Node
from pathlib import Path


def main():
    root = Root()
    node1 = Node("Hello", None, None, None)
    node2 = Node("World", None, None, None)
    root.create_node(Path("/"), node1)
    root.create_node(Path("/"), node2)
    print(root.serialize_path(2))

if __name__ == "__main__":
    main()
