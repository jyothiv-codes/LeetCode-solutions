class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        position=[]
        answer=[]
        n=len(boxes)
        for i in range(n):
            if boxes[i]=="1":
                position.append(i)
        for i in range(n):
            sum_=0
            for index in position:
                distance=abs(i-index)
                sum_+=distance
            answer.append(sum_)
        return answer

        