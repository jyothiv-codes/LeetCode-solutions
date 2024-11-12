class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        s=0
        count=0
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in d:
                count+=d[s-k]
            d[s]=d.get(s,0)+1
        return count
        