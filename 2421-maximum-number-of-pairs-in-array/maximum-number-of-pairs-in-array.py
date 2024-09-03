class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        pairs,leftover=0,0
        while i<len(nums):

            if i<len(nums)-1 and nums[i]==nums[i+1]:
                pairs+=1
                i+=2
            else:
                leftover+=1
                i+=1
                
                    
        return [pairs,leftover]
            


        