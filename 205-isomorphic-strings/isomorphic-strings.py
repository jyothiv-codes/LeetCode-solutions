class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        index=0
        s1=""
        for ch in s:
            if ch not in d1:
                index+=1
                d1[ch]=index
            s1+=str(d1[ch])
        d2={}
        index=0
        s2=""
        for ch in t:
            if ch not in d2:
                index+=1
                d2[ch]=index
            s2+=str(d2[ch])
        if s1==s2:
            return True
        return False
        

        
        
        