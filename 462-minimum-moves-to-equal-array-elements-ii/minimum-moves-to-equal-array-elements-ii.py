class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        print(nums)
        if n==1:
            return 0
        if n==2:
            middle=int((nums[0]+nums[1])/2)
            print("middle",middle)
        else:    
            mid=int(n/2)
            if n%2!=0:
                middle=nums[mid]
            else:
                middle=int((nums[mid]+nums[mid-1])/2)
            print("middle to reach",middle)
        total=0
        for i in nums:
            if i>middle:
                total+=(i-middle)
            elif i<middle:
                total+=(middle-i)
        return total
        