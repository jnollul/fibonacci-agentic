#!/usr/bin/env python3
"""Print a Fibonacci number by its index."""

import argparse
from collections.abc import Sequence


def fibonacci(index: int) -> int:
    """Return the Fibonacci number at a zero-based index."""
    if index < 0:
        raise ValueError("index must be non-negative")
    previous, current = 0, 1
    for _ in range(index):
        previous, current = current, previous + current
    return previous


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print the Fibonacci number at INDEX, starting with 0."
    )
    parser.add_argument("index", type=int, help="zero-based Fibonacci index")
    args = parser.parse_args(argv)
    if args.index < 0:
        parser.error("index must be non-negative")

    print(fibonacci(args.index))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
