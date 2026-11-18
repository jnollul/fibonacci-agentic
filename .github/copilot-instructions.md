# Repository guidance

## Project shape

This is a small, dependency-free polyglot Fibonacci CLI project. The Python
implementation in `fibonacci_cli.py` is the primary implementation and owns
the `unittest` coverage in `test_fibonacci_cli.py`. Java, Haskell, and
PowerShell provide equivalent standalone CLIs:

- `Fibonacci.java`
- `fibonacci.hs`
- `fibonacci.ps1`

All implementations take exactly one zero-based, non-negative integer index,
print the result as decimal text, accept `+` or `-` syntax only where the
language implementation documents it, and exit with status `2` for usage or
invalid-index errors.

Python requires Python 3.10 or later. Java requires a JDK, Haskell requires
GHC with `runghc`, and the PowerShell script requires PowerShell.

## Build, run, and test commands

From the repository root:

```console
python -m unittest -v
python -m unittest -v test_fibonacci_cli.FibonacciTests.test_index_ten
python fibonacci_cli.py 10
```

Use `python3` instead of `python` if that is the installed command. The single-test
pattern is `python -m unittest -v <TestClass>.<test_method>`; it can also be
used with `test_fibonacci_cli.CommandLineTests.test_rejects_negative_index`.

Run the other implementations with:

```console
javac Fibonacci.java
java Fibonacci 10
runghc fibonacci.hs 10
pwsh -NoProfile -File ./fibonacci.ps1 10
```

There is no package manifest, build system, formatter, or linter configuration
at the repository root. Remove generated Java `.class` files before committing
source-only changes.

## Cross-language conventions

- Keep `Fibonacci(0) == 0` and `Fibonacci(10) == 55` consistent across every
  implementation.
- Reject negative indices and missing/extra arguments. Report invalid integer
  input separately from negative input where supported.
- Preserve arbitrary-precision behavior: Python 3 integers, Java `BigInteger`,
  Haskell `Integer`, and PowerShell `BigInteger` are intentional.
- Python's public implementation is `fibonacci(index)` plus `main(argv)`;
  `main()` should remain testable without process-global stdout/stderr changes.
- When changing CLI behavior, update Python tests and all standalone
  implementations that can express the behavior.
