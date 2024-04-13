class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        #numbers=list(set(numbers))
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return [i+1,j+1]
            elif s>target:
                j-=1
            else:
                i+=1
            
                

        