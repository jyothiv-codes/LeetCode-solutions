class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        i=0
        s=s.split(" ")
        used_words=[]
        used_pattern=[]
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            print(i,d)
            p=pattern[i]
            if p in d:
                if s[i]!=d[p]:
                    print(s[i],d[p])
                    return False
            else:
                if s[i] in used_words:
                    return False
                if p in used_pattern:
                    return False
                d[p]=s[i]
                used_words.append(s[i])
                used_pattern.append(p)
        print(used_pattern)
        return True
            
                

        