class Solution:
    def smallestNumber(self, pattern: str) -> str:
        s=""
        stack=[]
        for i in range(len(pattern)+1):
            stack.append(i+1)
            if i==len(pattern) or pattern[i]=='I':
                while stack:
                    s+=str(stack.pop())
        return s

        