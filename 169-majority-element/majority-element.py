class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        result=0
        for i in nums:
            if count==0:
                result=i
                count+=1
            elif i!=result:
                count-=1
            elif i==result:
                count+=1
        return result
        