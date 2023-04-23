import functools
import random
import unittest

from src.sorting import swap, selection_sort, bubble_sort
from src.comparison import SavingsAccount

def every(lyst):
    index = 1
    while index < len(lyst):
        if lyst[index] < lyst[index - 1]:
            return False
        index += 1
    return True


class SortingTests(unittest.TestCase):
    def test_swap(self):
        lyst = [5, 3, 1, 2, 4]
        swap(lyst, 1, 4)
        self.assertEqual(lyst[1], 4)
        self.assertEqual(lyst[4], 3)
        
    def test_selection_sort(self):
        lyst = [5, 3, 1, 2, 4]
        selection_sort(lyst)
        self.assertTrue(every(lyst))
    
    def test_bubble_sort(self):
        lyst = [5, 3, 1, 2, 4]
        bubble_sort(lyst)
        self.assertTrue(every(lyst))

    def test_sort_comparables(self):
        lyst = [
            SavingsAccount('Samuel', '1234'),
            SavingsAccount('Stephanie', '5678'),
            SavingsAccount('Jairo', '2345'),
            SavingsAccount('Mireya', '6789'),
        ]

        random.shuffle(lyst)
        selection_sort(lyst)
        self.assertTrue(every(lyst))

        random.shuffle(lyst)
        bubble_sort(lyst)
        self.assertTrue(every(lyst))
