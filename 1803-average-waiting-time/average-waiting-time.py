class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        x=customers[0][0]
        prev_wait=0
        curr=0
        total=0
        for i in range(len(customers)):
            end=customers[i][1]
            start=customers[i][0]
            if x>=start:
                wait_time=end+(x-start)
            else:
                wait_time=end
            total+=wait_time
            completed_at=start+wait_time
            x=completed_at
        print(total,len(customers),total/len(customers))
        return total/len(customers)
        