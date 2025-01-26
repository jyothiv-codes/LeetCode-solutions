class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        h={}
        maxLen=0
        while right<len(s):
            ch=s[right]
            h[ch]=h.get(ch,0)+1
            max_freq=max(h.values())
            change=(right-left+1)-max_freq
            if change<=k:
                maxLen=max(maxLen,right-left+1)
            else:
                h[s[left]]-=1
                left+=1
            right+=1
        return maxLen


        