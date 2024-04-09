class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_list=list(set(nums))
        nums_list.sort()
        count=0
        for i in range(1,len(nums_list)-1):
            if nums_list[i]>nums_list[i-1] and nums_list[i]<nums_list[i+1]:
                count+=nums.count(nums_list[i])
        return count
        