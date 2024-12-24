class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i=0
        mini=10**6
        while i+k-1<len(nums):
            low=nums[i]
            high=nums[i+k-1]
            print(low,high)
            mini=min(high-low,mini)
            i+=1
        return mini
        