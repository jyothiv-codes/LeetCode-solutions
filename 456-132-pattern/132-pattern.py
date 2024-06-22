class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_=nums[0]
        stack=[]
        for i in range(1,len(nums)):
            while len(stack)>0 and nums[i]>=stack[-1][0]:
                stack.pop()
            if len(stack)>0 and nums[i]>stack[-1][1]:
                return True
            stack.append([nums[i],min_])
            min_=min(min_,nums[i])
        
        return False
        