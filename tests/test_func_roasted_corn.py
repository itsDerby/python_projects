from unittest import TestCase

from chapter_five import func_roasted_corn
from chapter_five.func_roasted_corn import add_function


class test_func_roasted_corn(TestCase):
    def test_add_function_exist(self):
        result = add_function([15, 20, 25, 20, 10, 5])
        answer = 95
        self.assertEqual(answer, result)

    def test_that_numbers_can_multiply(self):
        answer = 7500000
        self.assertEqual(answer, func_roasted_corn.multiply([15, 20, 25, 20, 10, 5]))

    def testThatICanGetLargestNumberFromAList(self):
        answer = 25
        self.assertEqual(answer, func_roasted_corn.largest([15, 20, 25, 20, 10, 5]))
