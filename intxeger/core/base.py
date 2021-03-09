import random
from collections.abc import Sized
from typing import Dict, List


class Node(Sized):

    length = 0

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, idx: int) -> str:
        return self.get(idx)

    def get(self, idx: int) -> str:
        raise NotImplementedError()

    def sample(self, N: int = 1) -> List[str]:
        if N > self.length:
            raise ValueError()
        iterator = self.iterator()
        return [next(iterator) for _ in range(N)]

    def iterator(self, ordered: bool = False):
        if ordered:
            for i in range(self.length):
                yield self.get(i)
        else:
            pool: Dict[int, int] = {}
            lower, upper = 0, self.length - 1
            for _ in range(self.length):
                i = random.randint(lower, upper)
                x = pool.get(i, i)
                pool[i] = pool.get(lower, lower)
                lower += 1
                yield self.get(x)
