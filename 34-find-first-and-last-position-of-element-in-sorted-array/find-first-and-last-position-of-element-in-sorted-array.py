class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerLimit(target):
            low=0
            index=-1
            high=len(nums)-1
            while low<=high:
                mid=int((low+high)/2)
                if nums[mid]==target:
                    index=mid
                    high=mid-1
                elif target<nums[mid]:
                    high=mid-1
                elif target>nums[mid]:
                    low=mid+1
            return index
        def upperLimit(target):
            low=0
            index=-1
            high=len(nums)-1
            while low<=high:
                mid=int((low+high)/2)
                if target==nums[mid]:
                    index=mid
                    low=mid+1
                elif target>nums[mid]:
                    low=mid+1
                elif target<nums[mid]:
                    high=mid-1
            return index
        low=lowerLimit(target)
        high=upperLimit(target)
        return [low,high]
        

        

        