# fibonacci-agentic

A dependency-free command-line tool that prints the Fibonacci number at a
zero-based `INDEX`, starting with `0`.

## Requirements

Python 3.10 or later.

## Usage

```console
python fibonacci_cli.py 10
55
```

`INDEX` must be a non-negative integer. An index of `0` prints `0`.
Invalid or negative input is reported as a command-line error.

## Tests

Run the test suite with Python's built-in unittest runner:

```console
python -m unittest -v
```
