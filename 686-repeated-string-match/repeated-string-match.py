class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        i=1
        repeat=int(len(b)/len(a))
        while i<=(repeat+5):
            if b in a*i:
                return i
            else:
                i+=1
        return -1
            
        

        return -1
        