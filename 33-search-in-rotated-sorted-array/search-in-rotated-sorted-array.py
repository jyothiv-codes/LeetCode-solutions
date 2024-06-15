class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        n=len(nums)
        high=n-1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        while low<=high:
            mid=int((high+low)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

            
        return -1

        