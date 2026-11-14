import contextlib
import io
import unittest

from fibonacci_cli import fibonacci, main


class FibonacciTests(unittest.TestCase):
    def test_zero_index(self):
        self.assertEqual(fibonacci(0), 0)

    def test_index_ten(self):
        self.assertEqual(fibonacci(10), 55)

    def test_negative_index_is_rejected(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


class CommandLineTests(unittest.TestCase):
    def test_prints_requested_fibonacci_number(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main(["10"])

        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "55\n")

    def test_rejects_negative_index(self):
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors), self.assertRaises(SystemExit) as exit_info:
            main(["-1"])

        self.assertEqual(exit_info.exception.code, 2)
        self.assertIn("index must be non-negative", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
