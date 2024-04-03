class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        sentence1="".join(word1)
        sentence2="".join(word2)
        if sentence1==sentence2:
            return True
        return False
        