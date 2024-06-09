class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged=[]
        intervals.sort()
        for interval in intervals:
            if len(merged)==0:
                merged.append(interval)
            else:
                end=merged[-1][1]
                curr_start=interval[0]
                curr_end=interval[1]
                if curr_start==end or curr_start<end:
                    merged[-1][1]=max(curr_end,end)
                elif curr_start>end:
                    merged.append(interval)
        return merged

        