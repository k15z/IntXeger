from typing import Sequence

from intxeger.core import Node


class Choice(Node):
    def __init__(self, choices: Sequence[Node]):
        self.choices = choices

    def length(self):
        return sum(len(choice) for choice in self.choices)

    def get(self, idx: int):
        if len(self) <= idx:
            raise IndexError()
        for choice in self.choices:
            if len(choice) <= idx:
                idx -= len(choice)
            else:
                return choice.get(idx)
