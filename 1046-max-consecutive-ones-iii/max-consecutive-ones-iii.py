class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window=0
        left=0
        right=0
        reset=0
        for right in range(len(nums)):  
            if nums[right] == 0:
                reset += 1  
            
            while reset > k:  
                if nums[left] == 0:
                    reset -= 1  
                left += 1  
                
            window = max(window, right - left + 1)  
       
        return window

        