
import heapq as hp
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_used=[]
        for i in range(len(heights)-1):
            difference=heights[i+1]-heights[i]
            if difference<=0:
                continue
            hp.heappush(ladders_used,difference)
            if len(ladders_used)<=ladders:
                continue
            bricks-=hp.heappop(ladders_used)
            if bricks<0:
                return i
        return len(heights)-1
       