import unittest

import pytest
from hypothesis import given
import hypothesis.strategies as st
from src.set_immutable  import *
from collections import Counter


class TestImmutableHashMap(unittest.TestCase):
    def test_size(self):
        set=NewSet()
        b=add(set,1)
        self.assertEqual(size(b), 1)
        b =add(b,1)
        self.assertEqual(size(b),1)
        b=add(b,2)
        self.assertEqual(size(b),2)
        b = add(b, None)
        self.assertEqual(size(b), 3)
        b = add(b, None)
        self.assertEqual(size(b), 3)
        # the size of set remained 0 so it is immutable
        self.assertEqual(set.size(), 0)


    def test_add(self):
        set=NewSet()
        b=add(set,1)
        self.assertEqual(to_list(b), [1])
        self.assertEqual(size(b),1)
        b=add(b,2)
        self.assertEqual(to_list(b),[1,2])
        self.assertEqual(size(b),2)
        b = add(b, None)
        list_set = NewSet()
        list_set.from_list([1, 2, None])
        self.assertEqual(b, list_set)
        # the size of set remained 0 so it is immutable
        self.assertEqual(set.size(),0)



    def test_remove(self):
        set=NewSet()
        b=add(set,1)

        b=add(b,2)
        b=add(b,None)

        list_set = NewSet()
        list_set.from_list([1, 2, None])
        self.assertEqual(b, list_set)


        c=remove(b,None)
        self.assertEqual(c.to_list(), [1,2])
        # b not changed, so it is immutable
        self.assertEqual(b.to_list(), [1, 2,None])
        with pytest.raises(ValueError):
            c = remove(c, 4)



    def test_to_list(self):
        def compare(s, t): #Judge whether two lists contain the same elements
            return Counter(s) == Counter(t)
        set = NewSet()
        b=add(set,1)
        self.assertEqual(compare(to_list(b),[1]),True)
        b=add(b,2)
        self.assertEqual(compare(to_list(b),[1,2]),True)
        b = add(b, None)

        self.assertEqual(compare(to_list(b),[1,2,None]),True)


    def test_from_list(self):

        def compare(s, t): #Judge whether two lists contain the same elements
            return Counter(s) == Counter(t)
        data = [
            [],
            [1],
            [1,2],
            [1, 2,3],
            [1, 2, 3, None]
        ]
        for list in data:
            set=NewSet()
            b=from_list(set,list)
            self.assertEqual(compare(to_list(b),list),True)

        num = 1
        set_from_num = NewSet()
        with pytest.raises(TypeError):
            from_list(set_from_num,num)


    def test_find(self):
        def is_satisfied(x):
            if x%2==0:
                return True
            else:
                return False
        set=NewSet()
        set=from_list(set,[1,2,3,4])

        self.assertEqual(find(set,is_satisfied),[2,4])
        with pytest.raises(TypeError):
            find(set,1)


    def test_filter(self):
        def is_filtered(x):  # remove elements with a value less than 3 in the set
            if x<3:
                return True
            else:
                return False
        set = NewSet()
        set = from_list(set, [1, 2, 3, 4,5])
        set=filter(set,is_filtered)
        list = to_list(set)
        for num in range(0, set.size()):
            self.assertEqual(list[num], num+3)  # 1 and 2 were removed

        with pytest.raises(TypeError):
            filter(set,1)


    def test_map(self):
        def increment(x):
            return x+10
        set = NewSet()
        set = from_list(set, [1, 2, 3, 4, 5])
        set=map(set,increment)
        list = to_list(set)
        for num in range(0, set.size()):
            self.assertEqual(list[num], num+11)

        with pytest.raises(TypeError):
            map(set,1)

    def test_reduce(self):
        def plus_operation(a,b):
            return a+b
        set = NewSet()
        set = from_list(set, [1, 2, 3, 4, 5])
        self.assertEqual(reduce(set,plus_operation,10),25)

        with pytest.raises(TypeError):
            reduce(set,1,1)


    def test_mconcat(self):
        set1 = NewSet()
        set2 = NewSet()
        set3 = NewSet()

        set1 = from_list(set1, [1,2])
        set2 = from_list(set2, [3,4])
        set3 = from_list(set3, [1,2,3,4])

        res=mconcat(set1,set2)
        self.assertEqual(to_list(res),to_list(set3))





    @given(st.lists(st.integers()))
    def test_to_lis_from_list_equality(self,a):
        set = NewSet()
        news_a = []
        for i in a:
            if i not in a:
                news_a.append(i)
        b = from_list(set, news_a)
        c = to_list(b)
        self.assertEqual(c.sort(), news_a.sort())

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        set_a = from_list(NewSet(),a)
        set_b = from_list(NewSet(),b)
        set_c = from_list(NewSet(),c)
        a_b = mconcat(set_a, set_b)
        b_a = mconcat(set_b, set_a)
        self.assertEqual(a_b,b_a)
        b_c = mconcat(set_b, set_c)
        c_b = mconcat(set_c, set_b)
        self.assertEqual(b_c,c_b)
        a__b_c = mconcat(set_a, b_c)
        a_b__c = mconcat(a_b,set_c)
        self.assertEqual(a__b_c, a_b__c)

    @given(a=st.lists(st.integers()))
    def test_monoid_identity_element(self, a):
        set_a = from_list(NewSet(), a)
        none_a = mconcat(None, set_a)
        a_none = mconcat(set_a, None)
        self.assertEqual(none_a, a_none)
        self.assertEqual(none_a,set_a)

    @given(a=st.lists(st.integers()),c=st.lists(st.integers()))
    def test_immutability(self,a,c):
        # check immutability  after add an element
        set_a = from_list(NewSet(), a)
        set_a_copy=copy.deepcopy(set_a)
        add(set_a,1)
        self.assertEqual(set_a,set_a_copy)

        # check immutability  after remove an element
        set_c = from_list(NewSet(), c)
        set_c_copy = copy.deepcopy(set_c)
        if(set_c.size()>0):
            remove(set_c, set_c.to_list()[0])
            self.assertEqual(set_c, set_c_copy)



if __name__ =='__main__':
    unittest.main()

