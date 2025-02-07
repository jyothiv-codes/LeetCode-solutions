class Solution:
    def canJump(self, nums: List[int]) -> bool:
        s=0
        for i in nums:
            
            if s<0:
                return False
            if i>s:
                s=i
            s-=1
        return True

        