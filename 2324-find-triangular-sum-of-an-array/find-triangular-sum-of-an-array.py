class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        while len(nums)>1:
            temp=[]
            for i in range(len(nums)-1):
                s=(nums[i]+nums[i+1])%10
                temp.append(s)
            nums=temp
        return nums[0]

        