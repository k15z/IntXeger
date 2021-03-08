from typing import Sequence

from intxeger.core import Node


class Choice(Node):
    def __init__(self, choices: Sequence[Node]):
        self.choices = choices
        self.length = sum(choice.length for choice in self.choices)

    def get(self, idx: int):
        if self.length <= idx:
            raise IndexError()
        for choice in self.choices:
            if choice.length <= idx:
                idx -= choice.length
            else:
                return choice.get(idx)
