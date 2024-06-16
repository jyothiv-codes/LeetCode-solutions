from itertools import permutations
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        index=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            print(index)
            nums=nums.reverse()
            print(nums)
        else:
            for i in range(n-1,index,-1):
                if nums[i]>nums[index]:
                    nums[i],nums[index]=nums[index],nums[i]
                    break
            temp=nums[index+1:]
            temp=temp[::-1]
            nums[index+1:]=temp



        

                

        
        
        
