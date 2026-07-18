class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.hashmap):
            if k == key:
                self.hashmap[i] = (key, value)
                return
        self.hashmap.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.hashmap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.hashmap):
            if k == key:
                del self.hashmap[i]
                return