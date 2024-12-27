class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s==t:
            return True
        if len(t)<len(s):
            return False
        i=0
        j=0
        while i<len(t):
            while j<len(s):
                if i<len(t) and j<len(s):
                    if t[i]==s[j]:
                        j+=1
                    i+=1
                    if i==len(t) and j<len(s)-1:
                        return False
                else:
                    return False
            return True
        