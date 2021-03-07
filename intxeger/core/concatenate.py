from typing import Sequence

from intxeger.core import Node


class Concatenate(Node):
    def __init__(self, nodes: Sequence[Node]):
        self.nodes = nodes

    def length(self) -> int:
        value = 1
        for choice in self.nodes:
            value *= len(choice)
        return value

    def get(self, idx: int) -> str:
        values = []
        for choice in reversed(self.nodes):
            sub_idx = idx % len(choice)
            idx = idx // len(choice)
            values.append(choice.get(sub_idx))
        return "".join(reversed(values))
