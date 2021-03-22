import copy

def cons(hash_map, key, value):
    if hash_map == None:
        return None
    if key == None or value == None:
        return hash_map
    hash_map_copy=copy.deepcopy(hash_map)
    index = hash_map_copy.hash(key)
    if hash_map_copy.items[index]:
        for item in hash_map_copy.items[index]:
            if hash_map_copy.equals(key, item[0]):
                hash_map_copy.items[index].remove(item)
                break
    hash_map_copy.items[index].append((key, value))
    hash_map_copy.count += 1
    return hash_map_copy

def remove(hash_map,key):
    if hash_map == None:
        return None
    if key == None :
        return hash_map
    hash_map_copy=copy.deepcopy(hash_map)
    index = hash_map_copy.hash(key)
    if hash_map_copy.items[index]:
        for item in hash_map_copy.items[index]:
            if hash_map_copy.equals(key,item[0]):
                hash_map_copy.items[index].remove(item)
                hash_map_copy.count -= 1
                return hash_map_copy
    return hash_map_copy


def size(hash_map):
    if hash_map == None:
        return 0
    one_dimensional_len=len(hash_map.items)
    if one_dimensional_len==0:
        return 0
    count = 0;
    for item in hash_map.items:
        count+=len(item)
    return count


def from_list(hash_map, list):
    if hash_map == None:
        return None
    if list==None:
        return hash_map
    hash_map_copy=copy.deepcopy(hash_map)
    for item in list:
        hash_map_copy=cons(hash_map_copy,item[0], item[1])
    return hash_map_copy


def to_list(hash_map):
    if hash_map==None:
        return None
    res = []
    for list in hash_map.items:
        for item in list:
            res.append([item[0], item[1]])
    return res


def find(hash_map, is_satisfied):
    if hash_map == None:
        return None
    if is_satisfied == None:
        return hash_map
    res = []
    for list in hash_map.items:
        for item in list:
            if is_satisfied(item[1]):
                res.append([item[0], item[1]])
    return res


def filter(hash_map, is_filtered):
    if hash_map == None:
        return None
    if is_filtered == None:
        return hash_map
    hash_map_copy=copy.deepcopy(hash_map)
    for list in hash_map_copy.items:
        for item in list:
            if is_filtered(item[1]):
                hash_map_copy=remove(hash_map_copy,item[0])

    return hash_map_copy

def map(hash_map, func):
    if hash_map == None or func == None:
        return None
    hash_map_copy=copy.deepcopy(hash_map)
    for list in hash_map_copy.items:
        for item in list:
            hash_map_copy=cons(hash_map_copy,item[0],func(item[1]))
    return hash_map_copy


def reduce(hash_map, func, initial_state):
    if hash_map == None or func ==None or initial_state == None:
        return None
    state = initial_state
    for list in hash_map.items:
        for item in list:
            state = func(state, item[1])
    return state

def mempty():
    return None
