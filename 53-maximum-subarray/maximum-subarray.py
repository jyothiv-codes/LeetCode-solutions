class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        total=nums[0]
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            if total<curr:
                total=curr
        return total

        