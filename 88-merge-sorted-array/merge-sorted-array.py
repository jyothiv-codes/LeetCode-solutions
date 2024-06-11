class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=0,0,0
        while j<len(nums2) and i<m+n:
            if nums2[j]<nums1[i]:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
                k+=1
            else:
                i+=1
        i=m+k
        while j<n:
            nums1[i]=nums2[j]
            i+=1
            j+=1

        