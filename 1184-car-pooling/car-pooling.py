class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        buckets=[0]*1002
        for trip in trips:
            for i in range(trip[1],trip[2]):
                buckets[i]+=trip[0]
        for num in buckets:
            if num>capacity:
                return False
        return True
        