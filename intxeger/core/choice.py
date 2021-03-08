from typing import Sequence

from intxeger.core import Node


class Choice(Node):
    def __init__(self, choices: Sequence[Node]):
        self.choices = choices
        self.length = sum(choice.length for choice in self.choices)
        self._is_all_one = all(choice.length == 1 for choice in self.choices)

    def get(self, idx: int):
        if self.length <= idx:
            raise IndexError()
        if self._is_all_one:
            return self.choices[idx].get(0)
        for choice in self.choices:
            if choice.length <= idx:
                idx -= choice.length
            else:
                return choice.get(idx)

    def __str__(self):
        return (
            "Choice(\n  "
            + "\n".join(str(c) for c in self.choices).replace("\n", "\n  ")
            + "\n)"
        )
