class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        j=0
        n=len(nums)
        while i<len(nums) and j<len(nums):
            if nums[i]!=0:
                i+=1
            if nums[j]==0:
                j+=1
            if i<n and j<n and i<j:
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
    
        