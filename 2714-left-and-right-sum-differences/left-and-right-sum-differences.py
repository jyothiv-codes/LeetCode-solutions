class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[0]*n
        left=[0]*n
        right=[0]*n
        s=sum(nums)
        left[0]=0
        right[0]=s-nums[0]
        left_s=0
        right[n-1]=0
        left[n-1]=s-nums[-1]

        for i in range(1,n):
            left[i]=left[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]+nums[i+1]
        for i in range(n):
            print(i)
            answer[i]=abs(left[i]-right[i])
        return answer

        