from models.node import Node

class BaseCreateNodeError(RuntimeError):
    def __init__(self, path: str, node: Node, message: str):
        self.path = path
        self.node = node
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}/{self.node.name}: {self.message}"

class NodeIsAnItemError(BaseCreateNodeError):
    ...


class NodeIsAStorageError(BaseCreateNodeError):
    ...


class NodeAlreadyExistsError(BaseCreateNodeError):
    ...


class NodeDoesNotExistError(BaseCreateNodeError):
    ...


class BaseDeletingNodeError(RuntimeError):
    def __init__(self, path: str, message: str):
        self.path = path
        self.message = message

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


class DeletingRootNodeError(BaseDeletingNodeError):
    ...

class DeletingUnexistingNodeError(BaseDeletingNodeError):
    ...

class NodeIsNotEmptyError(BaseDeletingNodeError):
    ...

class NodeIsNotADirectoryError(BaseDeletingNodeError):
    ...

class EmptyPathError(RuntimeError):
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message