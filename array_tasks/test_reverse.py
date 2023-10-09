from unittest import TestCase

from array_tasks import array_snack


class Test(TestCase):
    def test_reverse_array(self):
        my_array = [1, 2, 4, 5, 3]
        my_array2 = [3, 5, 4, 2, 1]
        self.assertEqual(my_array2, array_snack.reverse_array(my_array))
