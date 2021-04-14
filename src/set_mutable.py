import copy
from hash_map import *
class NewSet(object):

    def __init__(self):
        self.hash_map=NewHash() #based hash map
        self.value = object()  # the value of based hashmap

    def __eq__(self, other):
        return   self.to_list().sort()== other.to_list().sort()


    def size(self):
        return self.hash_map.count

    def add(self,element):
        return self.hash_map.add(element,self.value)

    def remove(self,element):
        return self.hash_map.remove(element)

    def from_list(self,list):
        if list == None:
            return None
        for i in list:
            self.hash_map.add(i,self.value)

    def to_list(self):
        res=[]
        for list in self.hash_map.items:
            for item in list:
                res.append(item[0])
        return res

    def find(self,is_satisfied):
        if is_satisfied==None:
            return None
        res=[]
        for item in self.to_list():
            if is_satisfied(item):
                res.append(item)
        return res


    def filter(self,is_filtered):
        if is_filtered == None:
            return self
        for item in self.to_list():
            if is_filtered(item):
                self.remove(item)

    def map(self,func):
        if func == None:
            return self
        for item in self.to_list():
            self.add(func(item))
            self.remove(item)
        return True

    def reduce(self,func,initial_state):
        if func==None or initial_state == None:
            return None
        state=initial_state
        for item in self.to_list():
            state=func(state,item)
        return state

    def mconcat(self, set):
        if self is None and set is None:
            return None
        if set is None:
            return self
        if self is None:
            return set
        list_set_a=self.to_list()
        list_set_b=set.to_list()
        res = NewSet()
        for item in list_set_a:
            res.add(item)
        tem=copy.deepcopy(res)
        tem=tem.to_list()
        for item in list_set_b:
            if item not in tem:
                res.add(item)
        return res

    def __iter__(self):
        self.index = 0
        self.list = self.to_list()
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration()
        else:
            self.index += 1
            return self.list[self.index - 1]
