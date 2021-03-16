class NewHash(object):
    def __init__(self,length=10):
        self.length= length
        self.items=[[] for i in range(self.length)]  #Creat a list of lists
        self.count=0

    def hash(self,key):
        return  hash(key) % self.length


    def size(self):
        return self.count

    def equals(self,k1,k2):
        return k1==k2


    def find(self,func):
        res=[]
        for list in self.items:
            for item in list:
                if func(item[1]):
                    res.append([item[0],item[1]])
        return res

    def filter(self,func):
        for list in self.items:
            for item in list:
                if func(item[1]):
                    self.remove(item[0])

    def map(self,func):

        for list in self.items:
            for item in list:
                self.add(item[0],func(item[1]))
        return True

    def reduce(self,func,initial_state):
        state=initial_state
        for list in self.items:
            for item in list:
                state=func(state,item[1])
        return state




    def add(self,key,value):
        index=self.hash(key)
        if self.items[index]:     #if this index already got taken, we need to check the list whether the same key is exist, if so delete it.
            for item in self.items[index]:
                if self.equals(key,item[0]):
                    self.items[index].remove(item)
                    break
        self.items[index].append((key,value))  # add new item into the index list.
        self.count+=1
        return True

    def from_list(self,list):
        for i in list:
            self.add(i[0],i[1])

    def to_list(self):
        res=[]
        for list in self.items:
            for item in list:
                res.append([item[0],item[1]])
        return res

    def get(self,key):
        index=self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key, item[0]):
                    return item[1]
        return None


    def remove(self,key):
        index=self.hash(key)
        if self.items[index]:
            for item in self.items[index]:
                if self.equals(key,item[0]):
                    self.items[index].remove(item)
                    self.count -= 1
                    return True

        return False


    def __iter__(self):
        self.index=0
        self.list=self.to_list()
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration()
        else:
            self.index += 1
            return self.list[self.index - 1]

if __name__ =='__main__':
    a=NewHash()
    a.from_list([(1,"ccvb"),(3,'sdf'),("asdf","asdf")])

    for i in a:
        print(i)

