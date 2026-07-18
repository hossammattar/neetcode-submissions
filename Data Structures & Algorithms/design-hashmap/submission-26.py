class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:

            
        if any(k == key for k,v in self.hashmap):
            for k,v in self.hashmap:
                if k == key:
                    self.hashmap.remove((k,v))
                    break
            self.hashmap.append((key,value))
        if (key,value) not in self.hashmap:
            self.hashmap.append((key,value))

    def get(self, key: int) -> int:
        for (k,v) in self.hashmap:
            if k == key:
                return v

        else:
            return -1


    def remove(self, key: int) -> None:
        for (k,v) in self.hashmap:
            if k == key:
                self.hashmap.remove((k,v))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)