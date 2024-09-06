class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def edit(word1,word2,m,n):
            if m==0:
                return n
            if n==0:
                return m
            if word1[m-1]==word2[n-1]:
                return edit(word1,word2,m-1,n-1)
            else:
                return 1+min(
                    edit(word1,word2,m,n-1),
                    edit(word1,word2,m-1,n),
                    edit(word1,word2,m-1,n-1)
                )
        

        return edit(word1,word2,len(word1),len(word2))
        