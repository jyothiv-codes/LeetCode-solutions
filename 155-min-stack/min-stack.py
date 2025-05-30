from collections import deque
class MinStack:

    def __init__(self):
        self.stack=deque([])
        self.m=0

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            pair=[val,val]
            #self.m=val    
        else:
            pair=[val,min(val,self.stack[-1][1])]
            #self.m=min(val,self.m)
        self.stack.append(pair)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()