class Solution:
    def getSmallestString(self, s: str) -> str:
        l=[int(X) for X in s]
        i=0
        while i<len(l)-1:
            if (l[i]%2==0 and l[i+1]%2==0) and (l[i]>l[i+1]):
                l[i],l[i+1]=l[i+1],l[i]
                l=[str(x) for x in l]
                return "".join(l)
            elif (l[i]%2!=0 and l[i+1]%2!=0) and (l[i]>l[i+1]):
                l[i],l[i+1]=l[i+1],l[i]
                l=[str(x) for x in l]
                return "".join(l)
            i+=1
        return s
        