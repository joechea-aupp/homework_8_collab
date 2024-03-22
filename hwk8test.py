import unittest
from exercise1 import replace_last
from exercise2 import index_power
from exercise3 import remove_all_after
from exercise4 import chunking_by
from exercise5 import reverse_ascending

class TestExercises(unittest.TestCase):

    # Exercise 1
    def test_exercise1_edge_cases(self):
        
        # 1) Testing an empty list
        self.assertEqual(replace_last([]), [])
        
        # 2) Testing a list with only one element
        self.assertEqual(replace_last([-2]), [-2])

    # Exercise 2
    def test_exercise2_edge_cases(self):
        
        # 1) Testing a list with negative numbers
        self.assertEqual(index_power([-1, -2, -3, -4], 2), 9)
        
        # 2) Testing a negative index
        self.assertEqual(index_power([1, 2, 3, 4], -2), -1)

        # 3) Testing when N is within the range of the array
        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)

        # 4) Testing when N is outside the range of the array
        self.assertEqual(index_power([1, 2, 3, 4], 5), -1)

        # 5) Testing an empty array
        self.assertEqual(index_power([], 1), -1)

        # 6) Testing an array with zero
        self.assertEqual(index_power([0, 1, 2, 3], 0), 1)

    # Exercise 3
    def test_exercise3_edge_cases(self):
        
        # 1) Testing a list with identical elements
        self.assertEqual(remove_all_after([1, 1, 1, 1], 1), [1])
        
        # 2) Testing a non-existent element to remove after
        self.assertEqual(remove_all_after([1, 1, 1, 1], 2), [1, 1, 1, 1])

        # 3) Testing an empty list
        self.assertEqual(remove_all_after([], 1), [])
        
    # Exercise 4
    def test_exercise4_edge_cases(self):

        # 1) Testing a chunk size that is half of the list size 
        self.assertEqual(chunking_by([1, 1, 1, 1], 2), [[1, 1], [1, 1]])
        
        # 2) Testing a chunk size larger than the list size
        self.assertEqual(chunking_by([1, 1, 1, 1], 5), [[1, 1, 1, 1]])
        
        # 3) Testing an empty list
        self.assertEqual(chunking_by([], 5), [])
        
        # 4) Testing a chunk size less than the list size, but not a divisor of the list size
        self.assertEqual(chunking_by([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])

        # 5) Testing a chunk size exactly the list size
        self.assertEqual(chunking_by([1, 2, 3, 4, 5], 5), [[1, 2, 3, 4, 5]])

        # 6) Testing a chunk size of 1
        self.assertEqual(chunking_by([1, 2, 3, 4, 5], 1), [[1], [2], [3], [4], [5]])

    # Exercise 5
    def test_exercise5(self):
        
        # 1) Testing a list with identical elements
        self.assertEqual(list(reverse_ascending([1, 1, 1, 1])), [1, 1, 1, 1])
        
        # 2) Testing a list with elements in descending order
        self.assertEqual(list(reverse_ascending([5, 4, 3, 2, 1])), [5, 4, 3, 2, 1])

        # 3) Testing a list with one maximal strictly ascending subsequence
        self.assertEqual(list(reverse_ascending([1, 2, 3, 2])), [3, 2, 1, 2])

        # 4) Testing a list with multiple maximal strictly ascending subsequences
        self.assertEqual(list(reverse_ascending([1, 2, 3, 1, 2, 3, 4])), [3, 2, 1, 4, 3, 2, 1])

        # 5) Testing a list with no strictly ascending subsequences
        self.assertEqual(list(reverse_ascending([2, 2, 2, 2])), [2, 2, 2, 2])

        # 6) Testing an empty list
        self.assertEqual(list(reverse_ascending([])), [])
        
if __name__ == '__main__':
    unittest.main()