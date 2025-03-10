from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value=self.cache[key]
            del self.cache[key]
            self.cache[key]=value
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache)==self.capacity:
                self.cache.popitem(last=False)
        if key in self.cache:
            del self.cache[key]
        self.cache[key]=value


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)