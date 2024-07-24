class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        days=[0]*n
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                element,index=stack.pop()
                days[index]=i-index
            stack.append([t,i])
        
        return days

        