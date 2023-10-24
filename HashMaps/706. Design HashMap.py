class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.hashset = [None] * self.capacity

    def add(self, key: int) -> None:
        index = self.hash(key)

        while True:
            if self.hashset[index] is None:
                self.hashset[index] = pai
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.hashset[index].key == key:
                self.hashset[index].value = key
                return
            
            index = (index + 1) % self.capacity




    def remove(self, key: int) -> None:
        if self.contains(key) is False:
            return
        index = self.hash(key)
        while self.hashset[index] is not None:
            if self.hashset[index].key == key:
                self.hashset[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity
        

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        while self.hashset[index] is not None:
            if self.hashset[index].key == key:
                return True
            index = (index + 1) % self.capacity
        return False

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
                self.add(p.key)
        




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)