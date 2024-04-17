class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for element in nums:
            if element not in hashmap:
                hashmap[element]=1
            else:
                return element
        