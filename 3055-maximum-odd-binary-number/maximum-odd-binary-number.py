class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones=s.count("1")
        zeros=s.count("0")
        new_s=""
        new_s+="1"*(ones-1)
        new_s+="0"*zeros
        new_s+="1"
        return new_s
        