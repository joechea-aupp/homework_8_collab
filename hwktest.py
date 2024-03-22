import unittest
from exercise1 import replace_last
from exercise2 import index_power
from exercise3 import remove_all_after
from exercise4 import chunking_by
from exercise5 import reverse_ascending

class TestExercises(unittest.TestCase):

    # Exercise 1
    def test_exercise1_edge_cases(self):
        
        # Testing edge cases for the replace_last function. 
        # Edge cases include a list with identical elements and a list with negative numbers.
        self.assertEqual(replace_last([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(replace_last([-2, -3, -4, -1]), [-1, -2, -3, -4])

    # Exercise 2
    def test_exercise2_edge_cases(self):
        
        # Testing edge cases for the index_power function. 
        # Edge cases include a list with negative numbers and a negative index.
        self.assertEqual(index_power([-1, -2, -3, -4], 2), 9)
        self.assertEqual(index_power([1, 2, 3, 4], -2), -1)

    # Exercise 3
    def test_exercise3_edge_cases(self):
        
        # Testing edge cases for the remove_all_after function. 
        # Edge cases include a list with identical elements and a non-existent element to remove after.
        self.assertEqual(remove_all_after([1, 1, 1, 1], 1), [1])
        self.assertEqual(remove_all_after([1, 1, 1, 1], 2), [1, 1, 1, 1])

    # Exercise 4
    def test_exercise4_edge_cases(self):
        
        # Testing edge cases for the chunking_by function. 
        # Edge cases include a chunk size that is half of the list size and a chunk size larger than the list size.
        self.assertEqual(chunking_by([1, 1, 1, 1], 2), [[1, 1], [1, 1]])
        self.assertEqual(chunking_by([1, 1, 1, 1], 5), [[1, 1, 1, 1]])

    # Exercise 5
    def test_exercise5_edge_cases(self):
        
        # Testing edge cases for the reverse_ascending function. 
        # Edge cases include a list with identical elements and a list with elements in descending order.
        self.assertEqual(list(reverse_ascending([1, 1, 1, 1])), [1, 1, 1, 1])
        self.assertEqual(list(reverse_ascending([5, 4, 3, 2, 1])), [5, 4, 3, 2, 1])
if __name__ == '__main__':
    unittest.main()