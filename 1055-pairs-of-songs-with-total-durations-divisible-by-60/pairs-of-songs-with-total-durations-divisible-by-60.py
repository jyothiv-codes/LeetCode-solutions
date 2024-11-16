class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        i=0
        for t in time:
            val=t%60
            d[val]=d.get(val,0)+1
        print(d)
        count=0
        for k in d:
            if 60-k in d:
                if 60-k!=k:
                    if d[k]>0 and d[60-k]>0:
                        count+=(d[k]*d[60-k])
                        print("not equal",k)
                        d[k]=0
                        d[60-k]=0
                else:
                    if d[k]>0:
                        n=d[k]
                        count+=(n*(n-1)/2)
                        d[k]-=int(d[k])
                        print("equal",k)
            elif k==0:
                if d[k]>0:
                    n=d[k]
                    count+=(n*(n-1)/2)
                    d[k]-=int(d[k])
                    

            
            
        print(count)
        return int(count)

