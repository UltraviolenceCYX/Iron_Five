import unittest

from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append('../../src')
from hash_map_mutable import *

class TestHash(unittest.TestCase):
    def test_size(self):
        self.assertEqual(NewHash().size(),0)
        self.assertEqual(NewHash().add(1,'1').size(),1)
        self.assertEqual(NewHash().add(1,'1').add(2,'2').size(),2)

    def test_to_list(self):
        self.assertEqual(NewHash().to_list(),[])
        self.assertEqual(NewHash().add(1,'2').to_list(),[[1,'2']])
        self.assertEqual(NewHash().add(1,'2').add(2,'2').to_list(),[[1,'2'],[2,'2']])

    def test_from_list(self):
        data=[
            [],
            [[1,'1']],
            [[1,'1'],[2,'2']]
        ]
        for e in data:
            a=NewHash()
            a.from_list(e)
            self.assertEqual(a.to_list(),e)

    def test_map(self):
        a=NewHash()
        a.map(str)
        self.assertEqual(a.to_list(),[])

        a = NewHash()
        a.from_list( [[1,1],[2,2]])
        a.map(str)
        self.assertEqual(a.to_list(), [[1,'1'],[2,'2']])

        a = NewHash()
        a.from_list([[1, 1], [2, 2]])
        a.map(lambda  x:x+10)
        self.assertEqual(a.to_list(), [[1,11], [2,12]])

    def test_reduce(self):
        a=NewHash()
        self.assertEqual(a.reduce(lambda st,e:st+e,0),0)

        a = NewHash()
        a.from_list([[1, 1], [2, 2]])
        self.assertEqual(a.reduce(lambda st, e: st + e, 0), 3)

    def test_iter(self):
        x=[[1, 1], [2, 2]]
        a = NewHash()
        a.from_list(x)
        tmp=[]
        for e in a:
            tmp.append(e)
        self.assertEqual(x,tmp)
        self.assertEqual(a.to_list(),tmp)

    def test_add(self):
        self.assertEqual(NewHash().add(1, '1').to_list(), [[1, '1']])
        self.assertEqual(NewHash().add(1, '1').add(2, '2').to_list(),[[1, '1'], [2, '2']])

if __name__ =='__main__':
    unittest.main()