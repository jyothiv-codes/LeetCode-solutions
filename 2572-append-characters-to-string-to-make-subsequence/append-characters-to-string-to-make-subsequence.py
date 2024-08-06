class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length=0
        i=0
        j=0
        len_s=len(s)
        len_t=len(t)
        while i<len_s and j<len_t:
            if s[i]==t[j]:
                length+=1
                j+=1
            i+=1
        return len_t-length
                
        