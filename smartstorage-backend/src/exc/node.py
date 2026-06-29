from models.node import Node

class BaseCreateNodeError(RuntimeError):
    def __init__(self, path: str, node: Node, message: str):
        self.path = path
        self.node = node
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}/{self.node.name}, {self.message}"

class NodeIsAItemError(BaseCreateNodeError):
    ...

class NodeIsAStorageError(BaseCreateNodeError):
    ...


class NodeAlreadyExistsError(BaseCreateNodeError):
    ...


class NodeDoesNotExistError(BaseCreateNodeError):
    ...

