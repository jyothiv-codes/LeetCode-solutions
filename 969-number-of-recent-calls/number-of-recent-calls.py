class RecentCounter:

    def __init__(self):
        self.queue=[]
        self.curr=-1
        self.length=0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.length+=1
        if self.curr==-1:
            self.curr=0
        if t-self.queue[self.curr]>3000:
            while t-self.queue[self.curr]>3000:
                self.curr+=1
        return self.length-self.curr
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)