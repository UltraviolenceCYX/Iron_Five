

def cons(hash_map, key, value):
    index = hash_map.hash(key)
    if hash_map.items[index]:
        for item in hash_map.items[index]:
            if hash_map.equals(key, item[0]):
                hash_map.items[index].remove(item)
                break
    hash_map.items[index].append((key, value))
    hash_map.count += 1
    return hash_map

def remove(hash_map,key):
    index = hash_map.hash(key)
    if hash_map.items[index]:
        for item in hash_map.items[index]:
            if hash_map.equals(key,item[0]):
                hash_map.items[index].remove(item)
                hash_map.count -= 1
                return True
    return False


def size(hash_map):
    one_dimensional_len=len(hash_map.items)
    if one_dimensional_len==0:
        return 0
    count = 0;
    for item in hash_map.items:
        count+=len(item)
    return count


def from_list(hash_map, list):
    for item in list:
        cons(hash_map,item[0], item[1])


def to_list(hash_map):
    res = []
    for list in hash_map.items:
        for item in list:
            res.append([item[0], item[1]])
    return res


def find(hash_map, is_satisfied):
    res = []
    for list in hash_map.items:
        for item in list:
            if is_satisfied(item[1]):
                res.append([item[0], item[1]])
    return res


def filter(hash_map, is_filtered):
    for list in hash_map.items:
        for item in list:
            if is_filtered(item[1]):
                remove(hash_map,item[0])

    return hash_map

def map(hash_map, func):
    for list in hash_map.items:
        for item in list:
            cons(hash_map,item[0],func(item[1]))
    return hash_map


def reduce(hash_map, func, initial_state):
    state = initial_state
    for list in hash_map.items:
        for item in list:
            state = func(state, item[1])
    return state

