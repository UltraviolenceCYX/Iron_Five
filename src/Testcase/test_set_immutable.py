import unittest

from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append('../../src')
from set_immutable import *


class TestImmutableHashMap(unittest.TestCase):
    def test_size(self):
        set=NewSet()
        set.add(1)
        self.assertEqual(size(set), 1)
        set.add(1)
        self.assertEqual(size(set),1)
        set.add(2)
        self.assertEqual(size(set),2)


    def test_add(self):
        set=NewSet()
        set.add(1)
        self.assertEqual(to_list(set), [1])
        self.assertEqual(size(set),1)
        set.add(2)
        self.assertEqual(to_list(set),[1,2])
        self.assertEqual(size(set),2)

    def test_remove(self):
        set=NewSet()
        set.add(1)
        set.add(2)

        self.assertEqual(to_list(remove(set,1)), [2])
        self.assertEqual(size(remove(set,1)),1)

    def test_to_list(self):
        set = NewSet()
        set.add(1)
        self.assertEqual(to_list(set), [1])
        set.add(2)
        self.assertEqual(to_list(set), [1, 2])

    @given(st.lists(st.integers))
    def test_from_list(self,a):
        print(a)
        # set = NewSet()
        # b=from_list(set,a)
        # self.assertEqual(to_list(b), a)