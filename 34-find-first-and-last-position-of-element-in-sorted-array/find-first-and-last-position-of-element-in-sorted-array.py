class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerLimit(low,high):
            index=-1
            while low<=high:
                mid=int(int(low+high)/2)
                if nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    index=mid
                    high=mid-1
            return index
        def higherLimit(low,high):
            index=-1
            while low<=high:
                mid=int(int(low+high)/2)
                if nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    index=mid
                    low=mid+1
            return index

                
                
        if target not in nums or len(nums)==0:
            return [-1,-1]
        if len(nums)==1:
            return [0,0]
        low=0
        high=len(nums)-1
        lower=lowerLimit(low,high)
        higher=higherLimit(low,high)
        return [lower,higher]


        