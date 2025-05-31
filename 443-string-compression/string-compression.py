class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            print([chars[0],str(1)])
            #return 2
            #return -1
        n=len(chars)
        output=[]
        i,curr=0,0
        while i<n:
            if i<n-1 and chars[i]==chars[i+1]:
                curr+=1
            else:
                output.append(chars[i])
                if curr!=0:
                    output.append(str(curr+1))
                curr=0
            i+=1
        """if chars[-1]!=chars[-2]:
            output.append(chars[-1])
            output.append(str(1))"""
        print("output arr",output)
        chars.clear()
        output="".join(output)
        print("length",chars)
        for ch in output:
            chars.append(ch)
        print(chars)
        #return len(chars)

        