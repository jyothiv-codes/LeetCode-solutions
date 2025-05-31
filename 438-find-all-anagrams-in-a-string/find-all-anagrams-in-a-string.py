from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output=[]
        dp=Counter(p)
        lp=len(p)
        for i in range(len(s)-lp+1):
            substr=s[i:i+lp]
            if Counter(substr)==dp:
            #if anagram(substr,dp):
                output.append(i)
        return output
        