import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles,k,h):
            time=0
            for pile in piles:
                time+=math.ceil(pile/k)
            return time<=h
        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            if canEat(piles,mid,h):
                high=mid
            else:
                low=mid+1
        return low

        
            
        

        