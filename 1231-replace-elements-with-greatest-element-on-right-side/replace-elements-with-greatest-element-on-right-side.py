class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        m=0
        for i in range(len(arr)-1,-1,-1):
            if i==len(arr)-1:
                result.append(-1)
                
            else:
                result.append(m)
            m=max(m,arr[i])
        return result[::-1]
        