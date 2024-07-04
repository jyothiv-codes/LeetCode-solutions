class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1={}
        d2={}
        for num in nums1:
            d1[num]=d1.get(num,0)+1
        for num in nums2:
            d2[num]=d2.get(num,0)+1
        inter=set(nums1).intersection(set(nums2))
        output=[]
        for num in inter:
            for count in range(min(d1[num],d2[num])):
                output.append(num)
        return output


        