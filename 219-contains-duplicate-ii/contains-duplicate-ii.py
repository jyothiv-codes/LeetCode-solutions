class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #this can be done using hashmap
        d={}
        for i in range(len(nums)):
            element=nums[i]
            if element in d:
                d[element].append(i)
            else:
                d[element]=[i]
        print(d)
        for row in d:
            list_=d[row]
            n=len(list_)
            print(d[row],n)
            for i in range(n-1):
                if (list_[i+1]-list_[i])<=k:
                    return True
        return False
                

        