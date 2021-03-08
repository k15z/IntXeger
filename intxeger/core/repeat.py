from intxeger.core import Node
from intxeger.core.choice import Choice
from intxeger.core.concatenate import Concatenate


class Repeat(Node):
    def __init__(self, node: Node, min_count: int = 0, max_count: int = 16):
        choices = []
        for count in range(min_count, max_count + 1):
            choices.append(Concatenate([node] * count))
        self.node = Choice(choices)
        self.length = self.node.length

    def get(self, idx: int) -> str:
        return self.node.get(idx)
