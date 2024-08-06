class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Assuming capacity and rocks are lists of the same length
        sorted_indices = sorted(range(len(capacity)), key=lambda i: capacity[i] - rocks[i])
        capacity = [capacity[i] for i in sorted_indices]
        rocks=[rocks[i] for i in sorted_indices]
        at_capacity=0
        i=0
        while additionalRocks>0:
            
            if i<len(capacity):
                if capacity[i]==rocks[i]:
                    at_capacity+=1
                    
                    
                else:
                    if additionalRocks<=capacity[i]-rocks[i]:
                        rocks[i]+=additionalRocks
                        additionalRocks=0
                        
                    else:
                        diff=capacity[i]-rocks[i]
                        rocks[i]+=diff
                        additionalRocks-=diff
                        
                    if capacity[i]==rocks[i]:
                        at_capacity+=1
                        
                        
                i+=1
            else:
                break
        
        return at_capacity



        