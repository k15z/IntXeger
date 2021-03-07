from intxeger.core import Node


class Constant(Node):
    def __init__(self, value: str):
        self.value = value

    def length(self) -> int:
        return 1

    def get(self, idx: int) -> str:
        if len(self) <= idx:
            raise IndexError()
        return self.value
