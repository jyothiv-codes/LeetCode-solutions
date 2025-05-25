class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            return int((nums[0]+nums[1])/2)
        nums.sort()
        print(nums)
        if n%2==0:
            middle=int((nums[int((n-1)/2)]+nums[int(n/2)])/2)
        else:
            middle=nums[int(n/2)]
        print("to reach",middle)
        total=0
        for i in nums:
            if i>middle:
                total+=(i-middle)
            elif i<middle:
                total+=(middle-i)
        return total