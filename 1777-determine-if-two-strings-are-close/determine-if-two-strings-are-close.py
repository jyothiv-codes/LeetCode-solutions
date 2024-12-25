class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1={}
        d2={}
        for ch in word1:
            d1[ch]=d1.get(ch,0)+1
        for ch in word2:
            d2[ch]=d2.get(ch,0)+1
        l1=[int(x) for x in d1.values()]
        l2=[int(x) for x in d2.values()]
        l1.sort()
        l2.sort()
        keys1=list(d1.keys())
        keys2=list(d2.keys())
        keys1.sort()
        keys2.sort()

        if l1==l2 and keys1==keys2:
            return True
        return False
        

        