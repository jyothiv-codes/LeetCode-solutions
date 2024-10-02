class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        m=0
        j=0
        i=0
        while i<(len(tasks)):
            temp=max(tasks[i:i+4])
            m=max(processorTime[j]+temp,m)
            i+=4
            j+=1
            
        return m
        