class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final=[]
        if len(intervals)==0:
            return [newInterval]
        merge=False
        for interval in intervals:
            print(final)
            start=interval[0]
            end=interval[1]
            if merge==False:
                if newInterval[0]>end:
                    final.append(interval)
                    #merge=True
                elif newInterval[0]<start and newInterval[1]<start:
                    final.append(newInterval)
                    final.append(interval)
                    merge=True 
                elif newInterval[0]<start and newInterval[1]>start:
                    newStart=min(start,newInterval[0])
                    newEnd=max(end,newInterval[1])
                    newInt=[newStart,newEnd]
                    final.append(newInt)
                    merge=True  
                elif newInterval[0]<=end:
                    newStart=min(start,newInterval[0])
                    newEnd=max(end,newInterval[1])
                    newInt=[newStart,newEnd]
                    
                    final.append(newInt)
                    merge=True
                    
                
                
                    
                else:
                 
                    final.append(interval)
                
            else:
                if start<=final[-1][1]:
                    final[-1][1]=max(end,final[-1][1])
            
                else:
                    final.append(interval)
                #final.append(interval)
        if merge==False:
            final.append(newInterval)
        return final

        