class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        curr=0
        for i in nums:
            if curr<0:
                return False
            elif i>curr:
                curr=i
            curr-=1
            
        return True
        