class MyStack(object):

    def __init__(self):
        self.queue=[]
        self.queue_len=0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.queue_len+=1
    
    def pop(self):
        """
        :rtype: int
        """
        i=0
        while i<self.queue_len:
            temp=self.queue.pop(0)
            if i<self.queue_len-1:
                self.queue.append(temp)
            i+=1
        self.queue_len-=1
        return temp

        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[self.queue_len-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue_len==0:
            return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()