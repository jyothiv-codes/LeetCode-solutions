class Solution:
    def fillCups(self, amount: List[int]) -> int:
        #amount.sort()
        seconds=0
        while amount.count(0)<3:
            amount.sort()
            if amount[0]>0 and amount[-1]>0:
                seconds+=1
                amount[0]-=1
                amount[-1]-=1
            elif amount[1]>0 and amount[-1]>0:
                seconds+=1
                amount[1]-=1
                amount[-1]-=1
            elif amount[1]>0 and amount[0]>0:
                seconds+=1
                amount[1]-=1
                amount[0]-=1
            else:
                if amount[0]>0:
                    seconds+=amount[0]
                    amount[0]=0
                if amount[1]>0:
                    seconds+=amount[1]
                    amount[1]=0
                if amount[2]>0:
                    seconds+=amount[2]
                    amount[2]=0
        return seconds

        