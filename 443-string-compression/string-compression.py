class Solution:
    def compress(self, chars: List[str]) -> int:
        i=1
        count=0
        chars.append("1")
        while i<len(chars):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                if count==0:
                    pass
                else:
                    for j in range(count):
                        chars.pop(i-1)
                        i-=1
                   
                    for ch in str(count+1):
                        chars.insert(i,ch)
                        i+=1
                    print(chars)
                    #chars.insert(i,str(count+1))
                    
                count=0
            i+=1
        chars.pop()
        print(chars)
        return len(chars)
        