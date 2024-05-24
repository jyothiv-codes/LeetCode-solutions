class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        start=0
        end=-1
        flag=False
        for i in word:
            if i!=ch:
                end+=1
            else:
                flag=True
                end+=1
                break
        ans=[ch for ch in word]
        print(ans)
        if flag==True:
            while start<=end:
                temp=ans[start]
                ans[start]=ans[end]
                ans[end]=temp
                start+=1
                end-=1
        return "".join(ans)