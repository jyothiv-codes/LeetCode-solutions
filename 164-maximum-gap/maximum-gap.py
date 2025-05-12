class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        nums.sort()
        if n==2:
            return nums[1]-nums[0]
        m=0
        for i in range(1,n):
            m=max(m,nums[i]-nums[i-1])
        return m

        