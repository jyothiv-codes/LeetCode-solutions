class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if len(set(nums))==len(nums):
            return 0
        d={}
        index=0
        for i in nums:
            if i not in d:
                d[i]=[]
            d[i].append(index)
            index+=1
        count=0
        print(d)
        for key in d:
            if len(d[key])>1:
                for i in range(len(d[key])):
                    for j in range(i+1,len(d[key])):
                        if (d[key][i]*d[key][j])%k==0:
                            print(i,j)
                            count+=1
        return count
        