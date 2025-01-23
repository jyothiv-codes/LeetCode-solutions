class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        #print(l)
        while l[-1]=="":
            l.pop()
        return len(l[-1])
        