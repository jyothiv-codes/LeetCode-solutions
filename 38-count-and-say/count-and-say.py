from collections import OrderedDict
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def countSay(k,string):
            if string=="" and k==1:
                return "1"
            else:
                output=[]
                
                print("string",string,k)
                curr=string[0]
                curr_pair=[int(curr),0] #element in integer format, value
                for ch in string:
                    if ch==curr:
                        curr_pair[1]+=1
                    else:
                        output.append(curr_pair)
                        curr_pair=[int(ch),1]
                    curr=ch
                output.append(curr_pair)
                print(output)
                string_return=""
                for pair in output:
                    string_return+=str(pair[1])+str(pair[0])
                return string_return
                
        s=""
        for i in range(1,n+1):
            
            s=countSay(i,s)
            
        return s
        

                


        