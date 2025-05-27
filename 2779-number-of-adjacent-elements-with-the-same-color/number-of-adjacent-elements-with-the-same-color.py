class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        output=[]
        array=[0]*n
        total=0
        for index,color in queries:
            #prev_col=array[index]
            if array[index]!=0 and index>0 and array[index]==array[index-1]:
                total-=1
            if array[index]!=0 and index<n-1 and array[index]==array[index+1]:
                total-=1
            array[index]=color
            if array[index]!=0 and index>0 and array[index]==array[index-1]:
                total+=1
            if array[index]!=0 and index<n-1 and array[index]==array[index+1]:
                total+=1
            output.append(total)
        return output
        