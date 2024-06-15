class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        ans=""
        i=0
        n=len(part)
        while True:
            if part in s:
                index=s.index(part)
                s=s[0:index]+s[index+n:]
            else:
                return s

        