from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.store=SortedList()
        
    def book(self, startTime: int, endTime: int) -> bool:
        index=self.store.bisect_right((startTime,endTime))
        if (index>0 and self.store[index-1][1]>startTime) or (index<len(self.store) and self.store[index][0]<endTime):
            return False
        self.store.add((startTime,endTime))
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)