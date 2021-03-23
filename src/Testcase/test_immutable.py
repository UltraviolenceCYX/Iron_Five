import unittest
from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append('C:/Users/admin/Desktop/IRON FIVE/Iron_Five/src')
from hash_map_mutable import *
from hash_map_immutable import *


class TestImmutableHashMap(unittest.TestCase):

    def test_cons(self):
        hash_map = NewHash()
        cons(hash_map, 1, 1)
        cons(hash_map, 2, 2)
        res_list = to_list(hash_map)
        for num in range(0, size(hash_map)):
            self.assertEqual(res_list[num], [num+1, num+1])

    def test_remove(self):
        hash_map = NewHash()
        hash_map =cons(hash_map, 1, 1)
        hash_map =cons(hash_map, 2, 2)
        hash_map =cons(hash_map, 3, 3)
        hash_map=remove(hash_map, 2)
        res_list = to_list(hash_map)
        self.assertEqual(res_list[0], [1, 1])
        self.assertEqual(res_list[1], [3, 3])
        self.assertEqual(size(hash_map), 2)

    def test_size(self):
        self.assertEqual(size(NewHash()), 0)
        self.assertEqual(size(NewHash().add(1, 1)), 1)
        self.assertEqual(size(NewHash().add(1, 1).add(2, 2)), 2)

    def test_from_list(self):
        items = [
            [],
            [[1, 1]],
            [[1, 1], [2, 2]]
        ]
        for item in items:
            hash_map = NewHash()
            hash_map=from_list(hash_map, item)
            self.assertEqual(to_list(hash_map), item)

    def test_to_list(self):
        self.assertEqual(to_list(NewHash()), [])
        self.assertEqual(to_list(NewHash().add(1,2)),[[1,2]])
        self.assertEqual(to_list(NewHash().add(1,2).add(2,2)),[[1,2],[2,2]])


    def test_find(self):
        def is_satisfied(x):
            if x==2:
                return True
            else:
                return False
        hash_map=NewHash()
        hash_map=cons(hash_map,1,1)
        hash_map=cons(hash_map,2,2)
        hash_map=cons(hash_map,3,3)
        self.assertEqual(find(hash_map,is_satisfied),[[2,2]])

    def test_filter(self):
        def is_filtered(x):  # remove elements with a value less than 3 in the hash map
            if x<3:
                return True
            else:
                return False
        hash_map = NewHash()
        cons(hash_map, 1, 1)
        cons(hash_map, 2, 2)
        cons(hash_map, 3, 3)
        cons(hash_map, 4, 4)
        cons(hash_map, 5, 5)
        hash_map=filter(hash_map,is_filtered)
        list = to_list(hash_map)
        for num in range(0, size(hash_map)):
            self.assertEqual(list[num], [num + 3, num + 3])  # [1,1] and [2,2] were removed

    def test_map(self):
        def increment(x):
            return x+1
        hash_map = NewHash()
        hash_map = cons(hash_map, 1, 1)
        hash_map = cons(hash_map, 2, 2)
        hash_map = cons(hash_map, 3, 3)
        hash_map = cons(hash_map, 4, 4)
        hash_map = cons(hash_map, 5, 5)
        hash_map=map(hash_map,increment)
        list = to_list(hash_map)
        for num in range(0, size(hash_map)):
            self.assertEqual(list[num], [num+1, num + 2])  # test if the value of every key-value set has been added

    def test_reduce(self):
        def plus_operation(a,b):
            return a+b
        hash_map = NewHash()
        hash_map = cons(hash_map, 1, 1)
        hash_map = cons(hash_map, 2, 2)
        hash_map = cons(hash_map, 3, 3)
        hash_map = cons(hash_map, 4, 4)
        hash_map = cons(hash_map, 5, 5)
        self.assertEqual(reduce(hash_map,plus_operation,10),25)  # calculate the sum of the initial value 10 and all the values in the hash map


    def test_mconcat(self):
        hash_map_A = NewHash()
        hash_map_A = cons(hash_map_A, 1, 1)
        hash_map_A = cons(hash_map_A, 2, 2)
        hash_map_A = cons(hash_map_A, 3, 3)
        hash_map_A = cons(hash_map_A, 4, 4)
        hash_map_B = NewHash()
        hash_map_B = cons(hash_map_B, 5, 5)
        hash_map_B = cons(hash_map_B, 6, 6)
        hash_map_B = cons(hash_map_B, 7, 7)
        hash_map_B = cons(hash_map_B, 8, 8)
        hash_map_res=mconcat(hash_map_A,hash_map_B)
        self.assertEqual(size(hash_map_res),8) # Test the size of the merged hash table
        list = to_list(hash_map_res)
        for num in range(0, size(hash_map_res)):
            self.assertEqual(list[num], [num + 1, num + 1]) # Test each element value of the merged hash table

if __name__ =='__main__':
    unittest.main()