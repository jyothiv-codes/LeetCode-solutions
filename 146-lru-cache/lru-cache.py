from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.store=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        value=self.store.pop(key)
        self.store[key]=value
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
        else:
            if self.capacity<=len(self.store):
                self.store.popitem(last=False)
            
        self.store[key]=value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)