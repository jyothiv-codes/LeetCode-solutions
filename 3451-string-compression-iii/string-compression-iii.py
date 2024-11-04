class Solution:
    def compressedString(self, word: str) -> str:
        final_str=""
        i=0
        count=1
        inter=1
        curr_str=""
        while i<len(word):
            curr_str=word[i]
            if i<len(word)-1 and word[i]==word[i+1] and inter<9:
                count+=1
                curr_str=word[i]
                inter+=1
            
            else:
                final_str+=str(count)
                final_str+=curr_str
                count=1
                inter=1
                
            i+=1
        if len(word)>=2 and word[-1]==word[-2]:
            count=int(final_str[-2])
            string=final_str[-1]
            final_str=final_str[:-2]
            final_str+=str(count)
            final_str+=string
            
            
        print(final_str)
        return final_str




        