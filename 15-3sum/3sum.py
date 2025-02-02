class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=set()
        n=len(nums)
        nums.sort()
        i=0
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    triplet=(nums[i],nums[j],nums[k])
                    output.add(triplet)
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
        return list(output)


        