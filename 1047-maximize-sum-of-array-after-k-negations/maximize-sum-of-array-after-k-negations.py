class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        negative=[]
        nums.sort()
        print("before preprocessing",nums)
        for i in nums:
            if i<0:
                negative.append(True)
            else:
                negative.append(False)
        #preprocessing is complete
        i=0
        n=len(nums)
        reduce_count=0
        if True in negative:
            
            while reduce_count<k and i<len(nums) and True in negative:
                nums[i]=-nums[i]
                negative[i]=not(negative[i])
                reduce_count+=1
                i+=1
            if reduce_count==k:
                print("nums before return",nums)
                return sum(nums)
            nums.sort()
            while reduce_count<k:
                nums[0]=-nums[0]
                reduce_count+=1
        nums.sort()
        print("after algo",nums)

        while reduce_count<k:
            nums[0]=-nums[0]
            reduce_count+=1
        return sum(nums)


        