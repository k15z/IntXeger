from typing import Sequence

from intxeger.core import Node


class Concatenate(Node):
    def __init__(self, nodes: Sequence[Node]):
        self.nodes = nodes
        self.length = 1
        for choice in self.nodes:
            self.length *= choice.length

    def get(self, idx: int) -> str:
        values = []
        for choice in reversed(self.nodes):
            sub_idx = idx % choice.length
            idx = idx // choice.length
            values.append(choice.get(sub_idx))
        return "".join(reversed(values))

    def __str__(self):
        return (
            "Concatenate(\n  "
            + "\n".join(str(c) for c in self.nodes).replace("\n", "\n  ")
            + "\n)"
        )
