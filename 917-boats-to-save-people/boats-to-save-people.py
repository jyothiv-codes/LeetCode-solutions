class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people.sort()
        curr=limit
        left=0
        right=len(people)-1
        while left<=right:
            count+=1
            if people[left]+people[right]<=curr:
                left+=1
            right-=1
            
        
        
                
        return count

            
        