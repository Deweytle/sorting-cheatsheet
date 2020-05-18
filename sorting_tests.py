import unittest
from sorting_algorithms import *

class TestSortingMethods(unittest.TestCase):
    test_array = []
    sorted_array = [11, 12, 22, 25, 34, 64, 90]

    def setUp(self):
        self.test_array = [64, 34, 25, 12, 22, 11, 90]

    def test_bubble(self):
        bubble_sort(self.test_array)
        self.assertEqual(self.test_array,self.sorted_array)
    
    def test_recursive_bubble(self):
        recursive_bubble_sort(self.test_array)
        self.assertEqual(self.test_array,self.sorted_array)
    
    def test_selection(self):
        selection_sort(self.test_array)
        self.assertEqual(self.test_array,self.sorted_array)
    
    def test_insertion(self):
        insertion_sort(self.test_array)
        self.assertEqual(self.test_array,self.sorted_array)
    
    def test_recursive_insertion(self):
        recursive_insertion_sort_wrapper(self.test_array)
        self.assertEqual(self.test_array,self.sorted_array)

if __name__ == '__main__':
    unittest.main()