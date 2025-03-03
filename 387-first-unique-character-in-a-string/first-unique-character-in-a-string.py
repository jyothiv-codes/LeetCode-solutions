from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency=OrderedDict()
        i=0
        # construct a hashmap. character is the key and array values are the indexes where it occurs
        for ch in s:
            if ch not in frequency:
                frequency[ch]=[]
            frequency[ch].append(i)
            i+=1
        
        # for every key, check if the value is equal to 1. if yes, return that index
        for ch in frequency:
            if len(frequency[ch])==1:
                return frequency[ch][0]
        # if no character is repeated only once, return -1
        return -1
        
        

        