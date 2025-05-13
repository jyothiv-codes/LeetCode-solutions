class MapSum:

    def __init__(self):
        self.d={}

    def insert(self, key: str, val: int) -> None:
        self.d[key]=val
        
    def sum(self, prefix: str) -> int:
        sum_=0
        for key in self.d:
            if prefix in key[0:len(prefix)]:
                sum_+=self.d[key]
        return sum_
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)