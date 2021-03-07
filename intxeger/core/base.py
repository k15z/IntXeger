import random
from collections.abc import Sized
from typing import Dict, List


class Node(Sized):
    def __len__(self) -> int:
        return self.length()

    def __getitem__(self, idx: int) -> str:
        return self.get(idx)

    def length(self) -> int:
        raise NotImplementedError()

    def get(self, idx: int) -> str:
        raise NotImplementedError()

    def sample(self, N: int) -> List[str]:
        if N > self.length():
            raise ValueError()
        pool: Dict[int, int] = {}
        values: List[str] = []
        lower, upper = 0, self.length() - 1
        for _ in range(N):
            i = random.randint(lower, upper)
            x = pool.get(i, i)
            pool[i] = pool.get(lower, lower)
            lower += 1
            values.append(self.get(x))
        return values
