class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        st=""
        k=0 #number of concatenations
        for word in words:
            st+=word
            print(st)
            if s==st:
                return True
            
            
        return False 
        