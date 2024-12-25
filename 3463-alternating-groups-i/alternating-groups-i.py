class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        k=2
        i=0
        while i+k<len(colors):
            if colors[i]==colors[i+k] and colors[i]!=colors[i+1]:
                c+=1
            i+=1
        if i+k==len(colors):
            if colors[-2]==colors[0]  and colors[-1]!=colors[-2]:
                c+=1
            if colors[-1]!=colors[0] and colors[-1]==colors[1]:
                c+=1
        return c
        