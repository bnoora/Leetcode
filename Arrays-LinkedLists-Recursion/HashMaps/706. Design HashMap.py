class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashmap = [None] * self.size

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if self.hashmap[index] == None:
            self.hashmap[index] = Pair(key, value)
        else:
            curr = self.hashmap[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next == None:
                    break
                curr = curr.next
            curr.next = Pair(key, value)
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.hashmap[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.hashmap[index]
        prev = self.hashmap[index-1]

        if curr == None:
            return
        if curr.key == key:
            self.hashmap[index] = curr.next
        else:
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return
                curr = curr.next
                
        



