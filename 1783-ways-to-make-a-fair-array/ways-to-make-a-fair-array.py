class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even=sum(nums[::2])
        total_odd=sum(nums[1::2])
        prefix_even,prefix_odd=0,0
        count=0
        for i in range(len(nums)):
            if i%2==0:
                total_even-=nums[i]
            else:
                total_odd-=nums[i]
            new_odd=prefix_odd+total_even
            new_even=prefix_even+total_odd
            if new_odd==new_even:
                count+=1
            if i%2==0:
                prefix_even+=nums[i]
            else:
                prefix_odd+=nums[i]
        return count
        