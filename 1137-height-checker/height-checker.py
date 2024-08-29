class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unsorted_heights=heights.copy()
        heights.sort()
        print(unsorted_heights)
        print(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=unsorted_heights[i]:
                count+=1
        return count
        