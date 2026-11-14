#!/usr/bin/env python3
"""Print a requested number of Fibonacci terms."""

import argparse
from collections.abc import Iterator, Sequence


def fibonacci_terms(count: int) -> Iterator[int]:
    """Yield the first count Fibonacci numbers, starting with 0."""
    if count < 0:
        raise ValueError("count must be non-negative")

    previous, current = 0, 1
    for _ in range(count):
        yield previous
        previous, current = current, previous + current


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print the first COUNT Fibonacci numbers, starting with 0."
    )
    parser.add_argument("count", type=int, help="number of terms to print")
    args = parser.parse_args(argv)
    if args.count < 0:
        parser.error("count must be non-negative")

    print(" ".join(str(term) for term in fibonacci_terms(args.count)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
