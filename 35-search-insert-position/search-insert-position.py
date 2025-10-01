class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]<target:
            return len(nums)
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            print(low,high,mid,nums[mid])
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        print(low,mid,high)
        return low

        