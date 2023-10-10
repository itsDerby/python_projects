from unittest import TestCase
from chapter_five import cornflakes

class Test(TestCase):
    def test_reverse(self):
        tuple1 = (10, 20, 30, 40, 50,70, 60)
        tuple_reversed = (60, 70, 50, 40, 30, 20, 10)
        self.assertEqual(cornflakes.reverse(tuple1), tuple_reversed)

    def test_nested_tuple(self):
        numbers = ("Orange", [10, 20, 30], (5, 15, 25))
        result = cornflakes.nested_tuple(numbers)
        expected = ((0, 20), (1, 25))
        self.assertEqual(result, expected)

