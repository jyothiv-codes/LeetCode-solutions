class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_press=0
        longest_key=""
        prev=0
        for i in range(len(releaseTimes)):
            press=releaseTimes[i]-prev
            if press>longest_press:
                longest_press=press
                longest_key=keysPressed[i]
            elif press==longest_press:
                longest_key=max(keysPressed[i],longest_key)
            prev=releaseTimes[i]
        return longest_key


        