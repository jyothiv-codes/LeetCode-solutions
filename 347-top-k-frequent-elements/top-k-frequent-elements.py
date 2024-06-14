import heapq as hp
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        heap=[]
        for key in d:
            hp.heappush(heap,(d[key]*(-1),key))
        answer=[]
        for i in range(k):
            temp=hp.heappop(heap)
            answer.append(temp[1])
        return answer
        
        

        