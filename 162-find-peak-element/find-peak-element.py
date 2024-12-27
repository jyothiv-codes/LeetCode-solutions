class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=1
        n=len(nums)
        high=n-2
        if n>1 and nums[0]>nums[1]:
            return 0
        while low<=high:
            mid=int(low + (high - low) // 2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1
        return n-1   
        