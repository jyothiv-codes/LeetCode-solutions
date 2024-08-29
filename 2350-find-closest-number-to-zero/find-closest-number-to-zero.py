class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff=abs(0-nums[0])
        number=nums[0]
        for i in range(1,len(nums)):
            if abs(0-nums[i])<diff:
                diff=abs(0-nums[i])
                number=nums[i]
            elif abs(0-nums[i])==diff:
                number=max(number,nums[i])
        return number

        