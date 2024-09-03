class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [-1]
        i=0
        
        greater=[-1]*len(nums)
        while i<len(nums):
            j=i+1
            if j==len(nums):
                j=0
            rounds=0
            while j<len(nums):
                if nums[j]>nums[i]:
                    greater[i]=nums[j]
                    break
                else:
                    j+=1
                if j==len(nums):
                    if rounds==0:
                        rounds+=1
                        j=0
                    else:
                        break
            i+=1
        print(greater)
        return greater



        

        