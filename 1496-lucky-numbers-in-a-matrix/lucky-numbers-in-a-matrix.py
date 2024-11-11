class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        i=0
        j=0
        output=[]
        min_index_j=[]
        for row in matrix:
            min_index_j.append(row.index(min(row)))
        i=0
        for j in min_index_j:
            column = [row[j] for row in matrix]
            if max(column)==matrix[i][j]:
                output.append(matrix[i][j])
            i+=1
        print(output)
        return output

        

                    
        