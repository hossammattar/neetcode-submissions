class MyHashSet:

    def __init__(self):
        self.data  = [-1 for _ in range(int(1e4))]

    def add(self, key: int) -> None:
        hashing = lambda key:int(key%(1e4))
        if key in self.data:
            return
        if self.data[hashing(key)] == -1:
            self.data[hashing(key)] = key
        else:
            for i in range(int(1e4)):
                if(self.data[hashing(key)+i] == -1):
                    self.data[hashing(key)+i] = key
                    break
    def remove(self, key: int) -> None:
        hashing = lambda key:int(key%int(1e4))
        if not (key in self.data):
            return
        for i in range(int(1e4)):
            if(self.data[hashing(key)+i] == key):
                self.data[(hashing(key)+i)%int(1e4)] = None
                break

    def contains(self, key: int) -> bool:
        return key in self.data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)