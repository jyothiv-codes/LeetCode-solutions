class TimeMap:

    def __init__(self):
        self.keys={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {"timestamps": {}, "order": []}
        self.keys[key]["timestamps"][timestamp] = value
        self.keys[key]["order"].append(timestamp)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        order = self.keys[key]["order"]
        idx = bisect_right(order, timestamp)
        if idx == 0:
            return ""
        
        target_time = order[idx - 1]
        return self.keys[key]["timestamps"][target_time]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)