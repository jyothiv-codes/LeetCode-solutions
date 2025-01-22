
import heapq as hp
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        hp.heapify(heap)
        for i in arr:
            diff=abs(x-i)
            pair=[diff,i]
            hp.heappush(heap,pair)
        l=[]
        for i in range(k):
            if len(heap)>0:
                pair=hp.heappop(heap)
                l.append(pair[1])
        l.sort()
        return l
        