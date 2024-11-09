class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        for i in nums:
            if k-i==i:
                if i in d and d[i]>1:
                    d[i]-=2
                    count+=1
                    if d[i]==0:
                        del d[i]
            elif k-i in d and i in d:
                d[i]-=1
                d[k-i]-=1
                count+=1
                if d[i]==0:
                    del d[i]
                if d[k-i]==0:
                    del d[k-i]
        return count
        