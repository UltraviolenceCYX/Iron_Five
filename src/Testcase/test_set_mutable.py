import unittest

from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append('../../src')
from set_mutable import *

class TestMutableSet(unittest.TestCase):

    def test_size(self):
        set=NewSet()
        set.add(1)
        self.assertEqual(set.size(), 1)
        set.add(1)
        self.assertEqual(set.size(), 1)
        set.add(2)
        self.assertEqual(set.size(), 2)


    def test_add(self):
        set=NewSet()
        set.add(1)
        self.assertEqual(set.to_list(), [1])
        self.assertEqual(set.size(),1)
        set.add(2)
        self.assertEqual(set.to_list(),[1,2])
        self.assertEqual(set.size(),2)


    def test_remove(self):
        set=NewSet()
        set.add(1)
        set.add(2)
        set.remove(1)
        self.assertEqual(set.to_list(), [2])
        self.assertEqual(set.size(),1)

    def test_to_list(self):
        set = NewSet()
        set.add(1)
        self.assertEqual(set.to_list(), [1])
        set.add(2)
        self.assertEqual(set.to_list(), [1, 2])

    def test_from_list(self):
        data = [
            [],
            [1],
            [1,2],
            [1, 2,3],
        ]
        for list in data:
            set=NewSet()
            set.from_list(list)
            self.assertEqual(set.to_list(), list)


    def test_find(self):
        def is_satisfied(x):
            if x%2==0:
                return True
            else:
                return False
        set=NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        self.assertEqual(set.find(is_satisfied),[2,4])

    def test_filter(self):
        def is_filtered(x):  # remove elements with a value less than 3 in the set
            if x<3:
                return True
            else:
                return False
        set = NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.filter(is_filtered)
        list = set.to_list()
        for num in range(0, set.size()):
            self.assertEqual(list[num], num+3)  # 1 and 2 were removed

    def test_map(self):
        def increment(x):
            return x+10
        set = NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.map(increment)
        list = set.to_list()
        for num in range(0, set.size()):
            self.assertEqual(list[num], num+11)  # test if the value of every element has been added

    def test_reduce(self):
        def plus_operation(a,b):
            return a+b
        set = NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        self.assertEqual(set.reduce(plus_operation,10),25)  # calculate the sum of the initial value 10 and all the values in the set

if __name__ =='__main__':
    unittest.main()