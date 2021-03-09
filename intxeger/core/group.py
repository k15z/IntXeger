from intxeger.core import Node

GROUP_TO_VALUE = {}


class Group(Node):
    def __init__(self, node: Node, ref_id: int):
        self.node = node
        self.ref_id = ref_id
        self.length = self.node.length

    def get(self, idx: int) -> str:
        GROUP_TO_VALUE[self.ref_id] = self.node.get(idx)
        return GROUP_TO_VALUE[self.ref_id]

    def __str__(self):
        return "Group(" + str(self.node).replace("\n", "\n  ") + f", {self.ref_id})"


class GroupRef(Node):
    def __init__(self, ref_id: int):
        self.ref_id = ref_id
        self.length = 1

    def get(self, idx: int) -> str:
        return GROUP_TO_VALUE[self.ref_id]

    def __str__(self):
        return f"GroupRef({self.ref_id})"
