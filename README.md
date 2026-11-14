# fibonacci-agentic

A dependency-free command-line tool that prints the first `COUNT` Fibonacci
numbers, starting with `0`.

## Requirements

Python 3.10 or later.

## Usage

```console
python fibonacci_cli.py 10
0 1 1 2 3 5 8 13 21 34
```

`COUNT` must be a non-negative integer. A count of `0` prints an empty line.
Invalid or negative input is reported as a command-line error.

## Tests

Run the test suite with Python's built-in unittest runner:

```console
python -m unittest -v
```
