from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        list_=SortedList()
        left=right=length=0
        n=len(nums)
        while right<n:
            list_.add(nums[right])
            while left<=right and list_[-1]-list_[0]>limit:
                list_.remove(nums[left])
                left+=1
            length=max(length,right-left+1)
            right+=1
        return length

        
