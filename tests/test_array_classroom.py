from unittest import TestCase
from array_tasks import array_classroom


class Test(TestCase):
    def test_the_list_can_multiply_three_times(self):
        num = [3, 7, 2, 6, 5]
        answer = [27, 343, 8, 216, 125]
        self.assertEqual(array_classroom.cube(num), answer)
