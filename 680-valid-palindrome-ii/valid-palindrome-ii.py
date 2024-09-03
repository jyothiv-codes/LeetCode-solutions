class Solution:
    def validPalindrome(self, s: str) -> bool:
        count=0
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                str1=s[:i]+s[i+1:]
                str2=s[:j]+s[j+1:]
                return str1==str1[::-1] or str2==str2[::-1]
            
                
        return True



        