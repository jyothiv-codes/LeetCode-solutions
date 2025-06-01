class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for n in nums1:
            d[n]=d.get(n,0)+1
        output=[]
        for n in nums2:
            if n in d and n not in output:
                output.append(n)
        return output
        
        