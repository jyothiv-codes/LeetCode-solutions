class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        increasing=[]
        count=0
        should_increase=True
        if len(arr)<3:
            return False
        if arr[1]<arr[0]:
            return False
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                count+=1
            elif arr[i]==arr[i-1]:
                return False
        if arr[-1]>arr[-2] and count>0:
            count+=1
        print(count)
        if count==1:
            return True
        return False
            
            
        