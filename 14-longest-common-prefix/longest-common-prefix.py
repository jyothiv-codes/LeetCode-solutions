class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d={}
        for word in strs:
            i=len(word)-1
            while i>=0:
                d[word[:i+1]]=d.get(word[:i+1],0)+1
                #if word[:i+1] in d:
                    
                i-=1
        if len(d)==0:
            return ""
        m=max(d.values())
        if m!=len(strs):
            return ""
        string=""
        for key in d:
            if d[key]==m:
                if len(string)<len(key):
                    string=key
        print(d)
        return string


            

        