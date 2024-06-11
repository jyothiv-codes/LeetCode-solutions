class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        k=0
        while j<len(nums2) and i<m+n:
            #print(nums1)
            if nums2[j]<nums1[i]:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
                k+=1
            else:
                i+=1
        print(nums1,i,j)
        i=m+k
        print(nums1,i,j)
        while j<n:
            print(nums1,i,j,"within final loop")
            nums1[i]=nums2[j]
            i+=1
            j+=1
        print(nums1,i,j)

        