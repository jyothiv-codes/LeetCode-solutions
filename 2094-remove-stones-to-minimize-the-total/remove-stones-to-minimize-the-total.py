import heapq as hp
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        l=[(-1)*x for x in piles]
        hp.heapify(l)
        for i in range(k):
            mini=hp.heappop(l)*(-1)
            mini=mini-math.floor(mini/2)
            mini*=(-1)
            hp.heappush(l,mini)

        return sum(l)*(-1)

        