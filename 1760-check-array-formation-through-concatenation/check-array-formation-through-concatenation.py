class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d={}
        for piece in pieces:
            piece_str = ",".join(map(str, piece))
            d[piece_str]=d.get(piece_str,0)+1
        print(d)
        i=0
        temp=[]
        flag=False
        while i<len(arr):
            temp.append(arr[i])
                
            temp_str = ",".join(map(str, temp))
            if temp_str in d:
                temp=[]
                flag=True
            i+=1
        if i==len(arr) and temp==[] and flag==True:
            return True
        return False

        