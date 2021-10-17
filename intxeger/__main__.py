"""
Print strings that can match a regular expression
"""
import argparse
import re
import sys

import intxeger


def check_pattern(s):
    try:
        re.compile(s)
    except re.error as exc:
        raise argparse.ArgumentTypeError(exc)
    return s


def main(args=None):
    parser = argparse.ArgumentParser(
        prog="python -m intxeger" if sys.argv[0].endswith("__main__.py") else None,
        description=__doc__,
        allow_abbrev=False,
    )
    parser.add_argument(
        "regex",
        type=check_pattern,
        help="A regular expression.",
    )
    parser.add_argument(
        "--max-repeat",
        type=int,
        default=10,
        metavar="N",
        help="Maximum repetitions for '.' & '*' operators (default: %(default)s)",
    )
    parser.add_argument(
        "--order",
        choices=("asc", "desc", "random"),
        default="asc",
        help="Order in which to print expansions (default: %(default)s)",
    )
    terminators = parser.add_mutually_exclusive_group()
    terminators.add_argument(
        "--terminator",
        "-t",
        default="\n",
        metavar="STR",
        help="Terminate each expansion with string STR (default: %(default)r)",
    )
    terminators.add_argument(
        "-0",
        action="store_const",
        const="\0",
        dest="terminator",
        help="Terminate each expansion with a NUL character",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=intxeger.__version__,
    )
    args = parser.parse_args(args)

    regex = args.regex + re.escape(args.terminator)
    root_node = intxeger.build(regex, max_repeat=args.max_repeat)

    if args.order == "asc":
        iterator = root_node.iterator(ordered=True)
    elif args.order == "desc":
        iterator = (root_node[i] for i in range(root_node.length - 1, -1, -1))
    elif args.order == "random":
        iterator = root_node.iterator(ordered=False)

    for match in iterator:
        sys.stdout.write(match)
    sys.stdout.flush()

    raise SystemExit(0)


if __name__ == "__main__":
    main()  # pragma: no cover
