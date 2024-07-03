class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        start_map={}
        i=0
        for pair in intervals:
            start_map[pair[0]]=i
            i+=1
        print(start_map)
        sorted_intervals=sorted(intervals,key=lambda x:x[0])
        print(sorted_intervals)
        answer=[-1]*len(intervals)

        for i,interval in enumerate(intervals):
            index=bisect_left(sorted_intervals,[interval[1],-10**7])
            if index!=len(intervals):
                answer[i]=start_map[sorted_intervals[index][0]]
        return answer