import heapq as hp
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        for point in points:
            distance=point[0]**2+point[1]**2
            pair=[distance,point]
            l.append(pair)
        hp.heapify(l)
        ans=[]
        for i in range(k):
            node=hp.heappop(l)
            ans.append(node[1])
        return ans
        