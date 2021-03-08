from intxeger.core import Choice, Concatenate, Constant, Node, Repeat


def optimize(node: Node, level=10):
    original_node = node
    for _ in range(level):
        new_node = _optimize(node)
        if str(node) == str(new_node):
            break
        node = new_node
    assert node.length == original_node.length
    assert node.get(0) == original_node.get(0)
    return node


def _optimize(node: Node):
    if isinstance(node, Choice):
        node = Choice([_optimize(c) for c in node.choices])
        if len(node.choices) == 1:
            node = node.choices[0]
        elif all(isinstance(c, Choice) for c in node.choices):
            node = Choice([c for n in node.choices for c in n.choices])  # type: ignore

    elif isinstance(node, Concatenate):
        node = Concatenate([_optimize(c) for c in node.nodes])
        if len(node.nodes) == 1:
            node = node.nodes[0]
        elif all(isinstance(c, Constant) for c in node.nodes):
            node = Constant("".join(c.value for c in node.nodes))  # type: ignore

    elif isinstance(node, Repeat):
        node = node.node

    if node.length < 1024:
        is_flat = isinstance(node, Constant) or (
            isinstance(node, Choice)
            and all(isinstance(c, Constant) for c in node.choices)
        )
        if not is_flat:
            node = Choice([Constant(node.get(i)) for i in range(node.length)])
    return node
