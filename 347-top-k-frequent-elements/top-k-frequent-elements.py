class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        output=[]
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        i=0
        for key in sorted_d:
            if i<k:
                output.append(key[0])
                i+=1
            else:
                return output
        return output

        