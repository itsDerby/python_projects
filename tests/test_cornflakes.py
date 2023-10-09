from unittest import TestCase
from chapter_five import cornflakes

class Test(TestCase):
    def test_reverse(self):
        tuple1 = (10, 20, 30, 40, 50,70, 60)
        tuple_reversed = (60, 70, 50, 40, 30, 20, 10)
        self.assertEqual(cornflakes.reverse(tuple1), tuple_reversed)

