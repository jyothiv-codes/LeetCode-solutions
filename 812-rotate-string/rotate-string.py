class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(goal):
            if s[i]==goal[j]:
                if goal[j:]==s[i:]+s[:i]:
                    return True
            i+=1
        return False

        