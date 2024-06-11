class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        compare=strs[0]
        prefix=""
        flag=False
        i=len(compare)
        while i>0:
            for word in strs[1:]:
                if compare[0:i] in word[0:len(compare[0:i])]:
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                return compare[0:i]
            i-=1
        if len(strs)==1:
            return strs[0]
        return prefix
