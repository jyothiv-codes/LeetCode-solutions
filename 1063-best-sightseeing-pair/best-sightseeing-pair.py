class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m=0
        i_store=[values[0]]
        j_store=[0]
        n=len(values)
        for i in range(1,n):
            i_store.append(max(i_store[i-1],values[i]+i))
            j_store.append(values[i]-i)
        for i in range(1,n):
            m=max(j_store[i]+i_store[i-1],m)
        print(i_store)
        print(j_store)
        return m
       
        