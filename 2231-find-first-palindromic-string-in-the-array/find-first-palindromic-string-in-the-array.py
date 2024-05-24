class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            start=0
            end=len(word)-1
            assume=True
            while start<=end:
                if word[start]==word[end]:
                    start+=1
                    end-=1
                else:
                    assume=False
                    break
            if assume==True:
                return word
        return ""
                    

        