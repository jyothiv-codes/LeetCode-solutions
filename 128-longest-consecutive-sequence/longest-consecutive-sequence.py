class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        m=0
        for i in nums:
            if i not in s:
                s.add(i)
        for element in s:
            if element-1 in s:
                pass
            else:
                length=1
                while element+1 in s:
                    element+=1
                    length+=1
                m=max(m,length)
        return m

        
        


        