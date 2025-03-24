class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[[1],[1,1]]
        if rowIndex==0 or rowIndex==1:
            return l[rowIndex]
        for i in range(2,rowIndex+1):
            temp=[1]
            prev=l[-1]
            for j in range(len(prev)-1):
                s=prev[j]+prev[j+1]
                temp.append(s)
            temp.append(1)
            l.append(temp)
        print(l)
        return l[-1]

        