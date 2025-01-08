class Solution:
    def minChanges(self, s: str) -> int:
        change=0
        i=0
        while i<(len(s)-1):
            if "11" in s[i:i+2]:
                pass
            elif "00" in s[i:i+2]:
                pass
            else:
                change+=1
            i+=2
        return change
        