class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_=[]
        nums.sort()
        i=0
        while i<len(nums):
            a=nums[i]
            b=nums.pop()
            max_.append(a+b)
            i+=1
        return max(max_)
        