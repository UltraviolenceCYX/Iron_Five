import unittest

from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append('../../src')
import pytest
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
        set.add(None)
        self.assertEqual(set.size(), 3)
        set.add(None)
        self.assertEqual(set.size(), 3)



    def test_add(self):
        set=NewSet()
        set.add(1)
        self.assertEqual(set.to_list(), [1])
        self.assertEqual(set.size(),1)
        set.add(2)
        self.assertEqual(set.to_list(),[1,2])
        self.assertEqual(set.size(),2)
        set.add(None)
        self.assertEqual(set.size(), 3)
        list_set=NewSet()
        list_set.from_list([1, 2,None])
        self.assertEqual(set, list_set)



    def test_remove(self):
        set=NewSet()
        set.add(1)
        set.add(2)
        set.add(None)
        set.add(3)
        set.remove(1)
        set.remove(None)
        self.assertEqual(set.to_list(), [2, 3])
        self.assertEqual(set.size(), 2)
        with pytest.raises(ValueError):
            set.remove(4)


    def test_to_list(self):
        set = NewSet()
        set.add(1)
        self.assertEqual(set.to_list(), [1])
        set.add(2)
        self.assertEqual(set.to_list(), [1, 2])
        set.add(None)
        self.assertEqual(set.to_list(), [1, 2,None])

    def test_from_list(self):
        data = [
            [],
            [1],
            [1,2],
            [1, 2,3],
            [1, 2, 3,None],

        ]
        for list in data:
            set=NewSet()
            set.from_list(list)
            self.assertEqual(set.to_list(), list)


    def test_find(self):
        def is_satisfied(x):
            if x==None:
                return False
            if x%2==0:
                return True
            else:
                return False
        set=NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(None)
        self.assertEqual(set.find(is_satisfied),[2,4])

    def test_filter(self):
        def is_filtered(x):  # remove elements with a value less than 3 in the set
            if x == None:
                return True
            if x<3 :
                return True
            else:
                return False
        set = NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.add(None)
        set.filter(is_filtered)
        list = set.to_list()
        for num in range(0, set.size()):
            self.assertEqual(list[num], num+3)  # 1 and 2 were removed

    def test_map(self):
        def increment(x):
            if x == None:
                return 10
            else:
             return x+10
        set = NewSet()
        set.add(None)
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.map(increment)
        list = set.to_list()
        for num in range(0, set.size()):
            if list[num] == None:
                self.assertEqual(list[num], 10)
            else:
                self.assertEqual(list[num], num+10)  # test if the value of every element has been added

    def test_reduce(self):
        def plus_operation(a,b):
            if b == None:
                return a
            else:
                return a+b
        set = NewSet()
        set.add(1)
        set.add(2)
        set.add(3)
        set.add(4)
        set.add(5)
        set.add(None)
        self.assertEqual(set.reduce(plus_operation,10),25)  # calculate the sum of the initial value 10 and all the values in the set

    def test_mconcat(self):
        set1 = NewSet()
        set2 = NewSet()
        set3 = NewSet()

        set1.from_list( [1, 2])
        set2.from_list( [3, 4,None])
        set3.from_list( [1, 2, 3, 4,None])
        set1=set1.mconcat(set2)
        self.assertEqual(set1.to_list(), set3.to_list())

    def test_iter(self):
        list=[1,2,3,None]
        set = NewSet()
        set.from_list(list)
        tmp=[]
        for item in set:
            tmp.append(item)
        set_from_list=NewSet()
        set_from_list.from_list(tmp)
        self.assertEqual(set,set_from_list)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, test_list):
        set = NewSet()
        handled_test_list=[]
        for item in test_list:
            if item not in handled_test_list:
                handled_test_list.append(item)
        set.from_list(handled_test_list)
        transformed_test_list = set.to_list()
        self.assertEqual(handled_test_list.sort(), transformed_test_list.sort())

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        set_a=NewSet()
        set_b=NewSet()
        set_c=NewSet()
        set_a.from_list(a)
        set_b.from_list(b)
        set_c.from_list(c)
        a_b=set_a.mconcat(set_b)
        b_a=set_b.mconcat(set_a)
        self.assertEqual(a_b, b_a)
        b_c = set_b.mconcat(set_c)
        c_b = set_c.mconcat(set_b)
        self.assertEqual(b_c,c_b)
        a__b_c = set_a.mconcat(b_c)
        a_b__c = a_b.mconcat(set_c)
        self.assertEqual(a__b_c,a_b__c)

if __name__ =='__main__':
    unittest.main()