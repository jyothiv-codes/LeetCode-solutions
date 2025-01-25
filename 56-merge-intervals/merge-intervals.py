class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        final_ans=[]
        for interval in intervals:
            if len(final_ans)==0:
                final_ans.append(interval)
            start=interval[0]
            end=interval[1]
            if start<=final_ans[-1][1]:
                final_ans[-1][1]=max(end,final_ans[-1][1])
            
            else:
                final_ans.append(interval)
        return final_ans

        