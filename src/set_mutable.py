
from hash_map_mutable import *
class NewSet(object):

    def __init__(self):
        self.hash_map=NewHash() #based hash map
        self.value = object()  # the value of based hashmap

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ or self.to_dict() == other.to_dict()

    def size(self):
        return self.hash_map.count

    def add(self,element):
        if element == None:
            return self
        return self.hash_map.add(element,self.value)

    def remove(self,element):
        if element == None:
            return self
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
