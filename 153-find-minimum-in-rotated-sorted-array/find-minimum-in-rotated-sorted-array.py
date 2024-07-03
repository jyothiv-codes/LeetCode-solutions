class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=100000
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                m=min(nums[mid],m)
                high=mid-1
        return m
        