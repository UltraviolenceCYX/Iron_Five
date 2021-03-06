import copy
from builtins import *

from src.hash_map import *
from inspect import isfunction
class NewSet(object):

    def __init__(self):
        self.hash_map=NewHash() #based hash map
        self.value = object()  # the value of based hashmap

    def __eq__(self, other):
        self_copy=copy.deepcopy(self)
        other_copy = copy.deepcopy(other)
        if self.to_list().__contains__(None) and other.to_list().__contains__(None):
            self_copy.remove(None)
            other_copy.remove(None)
            return   self_copy.to_list().sort()== other_copy.to_list().sort()
        if not self.to_list().__contains__(None) and not other.to_list().__contains__(None):
            return self.to_list().sort() == other.to_list().sort()
        else:
            return False



    def size(self)->int:
        return self.hash_map.count

    def add(self,element:object)->bool:
        return self.hash_map.add(element,self.value)

    def remove(self,element:object)->bool:
        return self.hash_map.remove(element)

    def from_list(self,list:list):
        if type(list).__name__!='list':
            raise TypeError('Parameter must be list type!')
        if list == None:
            return None
        for i in list:
            self.hash_map.add(i,self.value)

    def to_list(self)->list:
        res=[]
        for list in self.hash_map.items:
            for item in list:
                res.append(item[0])
        return res

    def find(self,is_satisfied)->list:
        if not isfunction(is_satisfied):
            raise TypeError('Parameter must be function!')
        if is_satisfied==None:
            return None
        res=[]
        for item in self.to_list():
            if is_satisfied(item):
                res.append(item)
        return res


    def filter(self,is_filtered):
        if not isfunction(is_filtered):
            raise TypeError('Parameter must be function!')
        if is_filtered == None:
            return self
        for item in self.to_list():
            if is_filtered(item):
                self.remove(item)

    def map(self,func):
        if not isfunction(func):
            raise TypeError('Parameter must be function!')
        if func == None:
            return self
        for item in self.to_list():
            self.add(func(item))
            self.remove(item)
        return True

    def reduce(self,func,initial_state:int)->int:
        if not isfunction(func):
            raise TypeError('Parameter must be function!')
        if func==None or initial_state == None:
            return None
        state=initial_state
        for item in self.to_list():
            state=func(state,item)
        return state

    def mconcat(self, set):
        if set is None:
            return self
        else:
            if not isinstance(set,NewSet):
                raise TypeError('Parameter must be set!')
            else:
                list_set_a=self.to_list()
                list_set_b=set.to_list()
                for item in list_set_b:
                    if item not in list_set_a:
                        self.add(item)
                return self

    def mempty(self):
        return None

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
