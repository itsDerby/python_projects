from unittest import TestCase
from chapter_five import cornflakes

class Test(TestCase):
    def test_reverse(self):
        tuple1 = (10, 20, 30, 40, 50,70, 60)
        tuple_reversed = (60, 70, 50, 40, 30, 20, 10)
        self.assertEqual(cornflakes.reverse(tuple1), tuple_reversed)

    # def test_method_that_return_nested_tuple(self):
    #     tuplee2 = ("Orange", [10, 20, 30], (5, 15, 25))
    #     tuple2_output = ((0, 20), (1, 25))
    #     self.assertEqual(cornflakes.tuple2(tuplee2), tuple2_output)
    #
    # def test_that_the_function_unpacks(self):
    #     tuple3 = 15, 25, 60, 50, 30, 40, 45, 55
    #     tuple3_output = (55, 15)
    #     self.assertEqual(cornflakes.tuple3(tuple3), tuple3_output)