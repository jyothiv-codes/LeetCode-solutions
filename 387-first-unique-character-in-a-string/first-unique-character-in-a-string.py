class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        i=0
        for ch in s:
            if ch not in d:
                d[ch]=[]
            d[ch].append(i)
            i+=1
        for key in d:
            if len(d[key])==1:
                return d[key][0]
        return -1
        