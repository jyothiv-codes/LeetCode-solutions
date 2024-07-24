class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=0
        prev,next_=0,0
        for i in range(1,len(nums)-1):
            if nums[i-1]!=nums[i]:
                prev=nums[i-1]
            if nums[i+1]!=nums[i]:
                next_=nums[i+1]
            if nums[i]>prev and nums[i]>next_ and prev!=0 and next_!=0:
                print(i,"hill")
                count+=1
            if nums[i]<prev and nums[i]<next_ and prev!=0 and next_!=0:
                print(i,"valley")
                count+=1
        return count



        