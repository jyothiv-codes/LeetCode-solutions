import heapq as hp
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        arr=[]
        for key,value in d.items():
            #value=d[key]
            value=value*(-1)
            pair=(value,key)
            arr.append(pair)
        heap=hp.heapify(arr)
        output=[]
        for i in range(k):
            if i>=len(nums):
                break
            pair=hp.heappop(arr)
            output.append(pair[1])
        return output
            
        