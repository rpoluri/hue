"""Tests for josepy.errors."""
import unittest


class UnrecognizedTypeErrorTest(unittest.TestCase):
    def setUp(self):
        from josepy.errors import UnrecognizedTypeError
        self.error = UnrecognizedTypeError('foo', {'type': 'foo'})

    def test_str(self):
        self.assertEqual(
            "foo was not recognized, full message: {'type': 'foo'}",
            str(self.error))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
