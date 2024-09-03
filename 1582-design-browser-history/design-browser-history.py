class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr=0
        

    def visit(self, url: str) -> None:
        #self.history.append(url)
        self.curr+=1
        if self.curr<=len(self.history)-1:
            self.history[self.curr]=url
            self.history=self.history[:self.curr+1]
        else: 
            self.history.append(url)
        #
            


        

    def back(self, steps: int) -> str:
        if self.curr-steps>=0:
            actual=self.curr-steps
            self.curr=actual
        else:
            self.curr=0
        print("back",self.history[self.curr])
        return self.history[self.curr]

    
    def forward(self, steps: int) -> str:
        if self.curr+steps<=len(self.history)-1:
            actual=self.curr+steps
            self.curr=actual
        else:
            self.curr=len(self.history)-1
        print("forward",self.history[self.curr])
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)