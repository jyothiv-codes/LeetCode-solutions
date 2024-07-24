import heapq as hp
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort() #sorts by start time
        num=len(rides)
        for row in rides:
            row[2]+=row[1]-row[0]
        curr_profit,max_profit=0,0
        heap=[]
        for start,end,profit in rides:
            while heap and heap[0][0]<=start:
                element1,element2=hp.heappop(heap)
                curr_profit=max(curr_profit,element2)
            hp.heappush(heap,(end,curr_profit+profit))
            max_profit=max(max_profit,curr_profit+profit)
        return max_profit


        