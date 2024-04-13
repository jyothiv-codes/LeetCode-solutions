class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def freq_map(word):
            f={}
            
            for ch in word:
                f[ch]=f.get(ch,0)+1
            s=""
            sorted_f=dict(sorted(f.items()))
            for key in sorted_f:
                s=s+key+str(sorted_f[key])
            return s
        d={}
        for word in strs:
            key=freq_map(word)
            if key not in d:
                d[key]=[]
            d[key].append(word)
        output=[]
        for key in d:
            temp=[]
            for values in d[key]:
                temp.append(values)
            output.append(temp)
        return output
            

        