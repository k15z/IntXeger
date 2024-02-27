from typing import Sequence

from intxeger.core import Node, Choice


class CharacterClassChoice(Node):
    def __init__(self, node: Choice):
        self.node = node
        self.length = sum(choice.length for choice in self.node.choices)

    def get(self, idx: int):
        self.node.get(idx)

    def __str__(self):
        return (
            "CharacterClassChoice(\n  "
            + "\n".join(str(c) for c in self.node.choices).replace("\n", "\n  ")
            + "\n)"
        )
