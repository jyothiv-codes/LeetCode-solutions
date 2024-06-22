class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=max(nums)
        curr_max,curr_min=1,1
        for i in nums:
            if i==0:
                curr_max=1
                curr_min=1
            else:
                temp=curr_max
                curr_max=max(i*curr_max,i*curr_min,i)
                curr_min=min(i*temp,i*curr_min,i)
                answer=max(answer,curr_max)
        return answer