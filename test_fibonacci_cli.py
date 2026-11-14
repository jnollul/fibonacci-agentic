import contextlib
import io
import unittest

from fibonacci_cli import fibonacci_terms, main


class FibonacciTermsTests(unittest.TestCase):
    def test_first_seven_terms(self):
        self.assertEqual(list(fibonacci_terms(7)), [0, 1, 1, 2, 3, 5, 8])

    def test_zero_terms(self):
        self.assertEqual(list(fibonacci_terms(0)), [])

    def test_negative_count_is_rejected(self):
        with self.assertRaises(ValueError):
            list(fibonacci_terms(-1))


class CommandLineTests(unittest.TestCase):
    def test_prints_requested_terms(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = main(["5"])

        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "0 1 1 2 3\n")

    def test_rejects_negative_count(self):
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors), self.assertRaises(SystemExit) as exit_info:
            main(["-1"])

        self.assertEqual(exit_info.exception.code, 2)
        self.assertIn("count must be non-negative", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
