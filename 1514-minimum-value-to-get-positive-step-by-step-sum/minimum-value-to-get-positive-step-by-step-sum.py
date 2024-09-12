class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=0
        min_start=1
        for i in nums:
            prefix+=i
            min_start=max(min_start,1-prefix)
        return min_start
        