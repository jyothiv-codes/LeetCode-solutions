class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        s=0
        n=len(nums)
        m=float('inf')
        greater=False
        for r in range(n):
            s+=nums[r]
            print(l,r,s,m)
            while s>=target:
                greater=True
                #print("target",l,r)
                m=min(m,r-l+1)
                s-=nums[l]
                l+=1
            
        if m==float('inf'):
            return 0
        return m
        