class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        n=len(nums)
        count=0
        element=-1
        output=[]
        for num in nums:
            d[num]=d.get(num,0)+1
            if d[num]>int(n/3):
                if num not in output:
                    output.append(num)
        return output
        
        