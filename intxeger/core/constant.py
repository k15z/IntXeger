from intxeger.core import Node


class Constant(Node):
    def __init__(self, value: str):
        self.value = value
        self.length = 1

    def get(self, idx: int) -> str:
        if self.length <= idx:
            raise IndexError()
        return self.value

    def __str__(self):
        return f"Constant({self.value})"
