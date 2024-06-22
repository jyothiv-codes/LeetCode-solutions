class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        n=len(nums)
        total=sum(nums)
        base=0
        for i in range(n):
            base+=(i*nums[i])
        m=base
        prev=base
        print("total",total,"prev",prev)
        for i in range(1,n):
            val=prev+total-(n*nums[n-i])
            m=max(m,val)
            prev=val
        return m
            

            

        