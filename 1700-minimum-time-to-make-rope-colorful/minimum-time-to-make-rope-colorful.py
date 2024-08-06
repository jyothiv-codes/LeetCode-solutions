class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        i=0
        colors=list(colors)
        while i<len(colors)-1:
            if colors[i]==colors[i+1]:
                if neededTime[i]<neededTime[i+1]:
                    index=i
                else:
                    index=i+1
                time+=neededTime[index]
                colors.pop(index)
                neededTime.pop(index)
            else:
                i+=1
        print(time)
        return time
                
        