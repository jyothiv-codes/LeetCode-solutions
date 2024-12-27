class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s=""
        index=0
        prefix=""
        l1=len(str1)
        l2=len(str2)
        for i in str2:
            s+=i
            #print("now s",s)
            if s in str1 and s not in str2:
                
                return prefix
            if s in str2 and s not in str1:
                
                return prefix
            
            #check the prefix 
            
            c1=int(l1/(index+1))
            c2=int(l2/(index+1))
            
            if s*c1==str1 and s*c2==str2:
                
                #index+=1
                prefix=s
            index+=1
        return prefix        
            
            

        