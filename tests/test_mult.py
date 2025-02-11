import unittest
from my_multiplication_lib import *  # * only to test our api is properly defined

class TestMathFunctions(unittest.TestCase):
    """Tests for my_multiplication_lib package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_multiplication_common(self):
        """Test the common function."""
        self.assertEqual(common_multiplication(2, 3), 6)

    def test_fancy_multiplication(self):
        """Test the common function."""
        self.assertEqual(fancy_multiplication(1, 2, 3), 6)

    def test_shouldnt_provide_private_method_in_api(self):
        # Assert that importing _private_multiplication raises an error
        with self.assertRaises(ImportError):
            from my_multiplication_lib import _private_multiplication

    def test_shouldnt_provide_private_but_not_really_method_in_api(self):
        # Check that `private_but_not_really_multiplication` is NOT in the current globals (namespace)
        self.assertFalse(
            'private_but_not_really_multiplication' in list(globals().keys()),
            '"private_but_not_really_multiplication" should not be in the top-level API after import *'
        )

if __name__ == "__main__":
    unittest.main()