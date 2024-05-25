class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start=0
        end=len(nums)-1
        print(nums)
        while start<=end:
            if nums[start]<0 and nums[end]>0:
                if abs(nums[start])<nums[end]:
                    end-=1
                elif abs(nums[start])>nums[end]:
                    start+=1
                else:
                    return nums[end]
            else:
                return -1

        return -1
        