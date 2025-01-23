from collections import OrderedDict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1=OrderedDict()
        h2=OrderedDict()
        for ch in s:
            h1[ch]=h1.get(ch,0)+1
        for ch in t:
            h2[ch]=h2.get(ch,0)+1
        sv1 = OrderedDict(sorted(h1.items(), key=lambda item: item[1]))
        sv2 = OrderedDict(sorted(h2.items(), key=lambda item: item[1]))
        print(sv1)
        print(sv2)
        l1=list(sv1.keys())
        l2=list(sv2.keys())
        if len(l1)!=len(l2):
            return False
        print(l1)
        mapping={}
        for i in range(len(l1)):
            mapping[l1[i]]=l2[i]
        matchstr=""
        for ch in s:
            matchstr+=(mapping[ch])
        if matchstr==t:
            return True
        return False
    
        

        