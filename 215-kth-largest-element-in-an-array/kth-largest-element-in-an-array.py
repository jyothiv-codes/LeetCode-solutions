import heapq as hp
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)

        hp.heapify(nums)
        for i in range(n-k+1):
            temp=hp.heappop(nums)
        return temp

        