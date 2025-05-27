class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        def swap(n,m,row):
            row[n],row[m]=row[m],row[n]

        # let's handle it row by row 
        
        for row in boxGrid:
            #i=0
            for i in range(len(row)-1,-1,-1):
                if row[i]=="*" or row[i]==".": 
                    pass #ignore
                elif row[i]=="#":
                    # reach a point where there is a stone or it is the bottom of the box
                    k=i
                    while k<len(row)-1 and (row[k+1]!="#" and row[k+1]!="*"):
                        swap(k,k+1,row)
                        k+=1
        print(boxGrid)
        # take the transpose of this
        nrows=len(boxGrid)
        ncols=len(boxGrid[0])
        return [list(row)[::-1] for row in zip(*boxGrid)]






        