class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def calculate(word1,word2,m,n):
            if m==0:
                return n
            if n==0:
                return m
            if word1[m-1]==word2[n-1]:
                return calculate(word1,word2,m-1,n-1)
            else:
                return 1+min(calculate(word1,word2,m-1,n-1),
                calculate(word1,word2,m,n-1),
                calculate(word1,word2,m-1,n))
        return calculate(word1,word2,len(word1),len(word2))
        