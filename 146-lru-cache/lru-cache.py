from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.store=OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.store:
            value=self.store[key]
            del self.store[key]
            self.store[key]=value
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            val=self.store[key]
            del self.store[key]
        if self.capacity==len(self.store):
            self.store.popitem(last=False)
        self.store[key]=value




        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)