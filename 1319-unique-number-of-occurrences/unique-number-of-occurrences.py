class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        freq=[]
        for key in d:
            if d[key] in freq:
                return False
            freq.append(d[key])
        return True
        