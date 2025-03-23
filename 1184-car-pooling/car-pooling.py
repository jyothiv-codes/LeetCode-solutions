class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        buckets=[0]*1001
        for trip in trips:
            start=trip[1]
            end=trip[2]
            for k in range(start,end):
                buckets[k]+=trip[0]
        for bucket in buckets:
            if bucket>capacity:
                return False
        return True


            
        