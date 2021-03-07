# flake8: noqa
# mypy: ignore-errors
import sre_parse
import string

from intxeger.core import Choice, Concatenate, Constant, Node, Repeat

CATEGORY_MAP = {
    sre_parse.CATEGORY_SPACE: " \t\n\r\x0b\x0c",
    sre_parse.CATEGORY_NOT_SPACE: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
    sre_parse.CATEGORY_DIGIT: "0123456789",
    sre_parse.CATEGORY_NOT_DIGIT: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c",
    sre_parse.CATEGORY_WORD: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_",
    sre_parse.CATEGORY_NOT_WORD: "!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~ \t\n\r\x0b\x0c",
}


def _to_node(op, args):
    if op == sre_parse.IN:
        nodes = []
        for op, args in args:
            nodes.append(_to_node(op, args))
        return Choice(nodes)
    elif op == sre_parse.RANGE:
        min_value, max_value = args
        return Choice(
            [Constant(chr(value)) for value in range(min_value, max_value + 1)]
        )
    elif op == sre_parse.LITERAL:
        return Constant(chr(args))
    elif op == sre_parse.CATEGORY:
        return Choice([Constant(c) for c in CATEGORY_MAP[args]])
    elif op == sre_parse.ANY:
        return Choice([Constant(c) for c in string.printable])
    elif op == sre_parse.SUBPATTERN:
        nodes = []
        for op, args in args[3]:
            nodes.append(_to_node(op, args))
        return Concatenate(nodes)
    elif op == sre_parse.MAX_REPEAT:
        min_, max_, args = args
        op, args = args[0]
        if max_ == sre_parse.MAXREPEAT:
            return Repeat(_to_node(op, args), min_)
        return Repeat(_to_node(op, args), min_, max_)
    else:
        raise ValueError(f"{op} {args}")


def build(regex: str) -> Node:
    nodes = []
    tokens = sre_parse.parse(regex)
    for op, args in tokens:
        nodes.append(_to_node(op, args))
    return Concatenate(nodes)
