class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_index=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                one_index.append(i)
        output=[]
        temp=0
        print(one_index)
        for i in range(len(boxes)):
            temp=0
            for j in range(len(one_index)):
                temp+=abs(i-one_index[j])
            
            output.append(temp)
        print(output)
        return output

        