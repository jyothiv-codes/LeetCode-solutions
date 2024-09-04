class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashmap={}
        for ch in words[0]:
            hashmap[ch]=hashmap.get(ch,0)+1
        
        for word in words[1:]:
            to_delete=[]
            for key in hashmap:
                if key not in word:
                    to_delete.append(key)
                else:
                    hashmap[key]=min(hashmap[key],word.count(key))
            for key in to_delete:
                del hashmap[key]
        print(hashmap)
        s=""
        for key in hashmap:
            s+=(key*hashmap[key])
        return [ch for ch in s]


        