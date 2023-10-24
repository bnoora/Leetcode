class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.hashset = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.hashset[index] is None:
                self.hashset[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.hashset[index].key == key:
                self.hashset[index].value = value
                return
            
            index = (index + 1) % self.capacity




    def remove(self, key: int) -> None:
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.hashset[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity
        

    def get(self, key: int) -> bool:
        index = self.hash(key)
        while self.hashset[index] is not None:
            if self.hashset[index].key == key:
                return self.hashset[index].value
            index = (index + 1) % self.capacity
        return -1

    def hash(self, key):
        charidx = 0
        key = str(key)
        for i in key:
            charidx += ord(i)
        return charidx % self.capacity
    
    def rehash(self):
        self.capacity *= 2
        newhashset = [None] * self.capacity

        oldhashset = self.hashset
        self.hashset = newhashset
        self.size = 0
        for p in oldhashset:
            if p is not None:
                self.put(p.key, p.value)
        

