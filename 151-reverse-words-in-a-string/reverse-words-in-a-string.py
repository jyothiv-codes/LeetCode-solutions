class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        split_words=s.split(" ")
        split_words=split_words[::-1]
        print(split_words)
        ans=""
        for word in split_words:
            if word!="":
                ans+=word
                ans+=" "
        return ans[:-1]
        