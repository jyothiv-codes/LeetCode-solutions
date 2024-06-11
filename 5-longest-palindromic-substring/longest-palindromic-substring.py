class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=0
        answer=""
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>m:
                    m=r-l+1
                    answer=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>m:
                    m=r-l+1
                    answer=s[l:r+1]
                l-=1
                r+=1

        return answer



        