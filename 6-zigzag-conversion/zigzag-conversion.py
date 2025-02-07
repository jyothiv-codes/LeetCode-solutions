class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction=1
        if numRows==1:
            return s
        l=[""]*numRows
        i=0
        final=[[] for i in range(numRows)]
        print(final)
        for ch in s:
            print(i)
            if i==0:
                direction=1
            elif i==numRows-1:
                direction=-1
            final[i].append(ch)
            i+=direction
        print(final)
        ans=""
        for row in final:
            for ch in row:
                ans+=ch
        return ans

        