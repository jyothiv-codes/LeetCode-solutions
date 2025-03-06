class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l=list(s)
        while len(l)>2:
            n=len(l)
            temp=[]
            for i in range(n-1):
                s=(int(l[i])+int(l[i+1]))%10
                s=str(s)
                temp.append(s)
            l=temp
        if l[0]==l[1]:
            return True
        else:
            return False

        