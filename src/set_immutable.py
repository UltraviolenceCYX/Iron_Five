import copy
from src.set_mutable import *

def size(set:NewSet):
    return set.size()


def add(set:NewSet,element):

    if element == None :
        return set
    set_copy = copy.deepcopy(set)
    set_copy.add(element)
    return set_copy

def remove(set:NewSet,element):

    if element == None :
        return set
    set_copy = copy.deepcopy(set)
    set_copy.hash_map.remove(element)
    return set_copy


def from_list(set:NewSet,list):
    if list == None :
        return set
    if set is None:
        set_copy=NewSet()
    else:
        set_copy = copy.deepcopy(set)
    for i in list:
        set_copy.hash_map.add(i, object())
    return set_copy

def to_list(set:NewSet):
    res = []
    for list in set.hash_map.items:
        for item in list:
            res.append(item[0])
    return res

def find(set:NewSet,is_satisfied):
    if is_satisfied == None:
        return None
    res = []
    for item in set.to_list():
        if is_satisfied(item):
            res.append(item)
    return res

def filter(set:NewSet,is_filtered):
    if is_filtered == None:
        return None
    set_copy = copy.deepcopy(set)
    for item in set_copy.to_list():
        if is_filtered(item):
            set_copy.remove(item)
    return set_copy

def map(set:NewSet,func):
    if func == None:
        return None
    set_copy = copy.deepcopy(set)
    for item in set_copy.to_list():
        set_copy.add(func(item))
        set_copy.remove(item)
    return set_copy

def reduce(set:NewSet,func,initial_state):
    if func == None or initial_state == None:
        return None
    state = initial_state
    for item in set.to_list():
        state = func(state, item)
    return state

def mconcat(set1:NewSet,set2:NewSet):
    if set1 is None and set2 is None:
        return None
    if set2 is None:
        return set1
    if set1 is None:
        return set2

    s1=to_list(set1)
    s2=to_list(set2)

    res=NewSet()


    for item in s1:
        res=add(res,item)

    tem=res.to_list()

    for item in s2:
        if item not in tem:
            res=add(res,item)
    return res