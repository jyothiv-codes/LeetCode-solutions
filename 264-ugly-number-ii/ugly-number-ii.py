class Solution:
    def nthUglyNumber(self, n: int) -> int:
        output=[1]
        i,j,k=0,0,0
        count=0
        while count<n:
            val=min(output[i]*2,output[j]*3,output[k]*5)
            if val==output[i]*2:
                i+=1
            if val==output[j]*3:
                j+=1
            if val==output[k]*5:
                k+=1
            count+=1
            if count==n:
                return output[-1]
            output.append(val)
            
            

            
        