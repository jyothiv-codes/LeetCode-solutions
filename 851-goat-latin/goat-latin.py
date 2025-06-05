class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words=sentence.split(" ")
        n=len(words)
        ans=[]
        for i in range(n):
            word=words[i]
            if word[0] in ["a","e","i","o","u","A","E","I","O","U"]:
                temp=word+"ma"
            else:
                temp=word[1:]+word[0]+"ma"
            temp+="a"*(i+1)
            ans.append(temp)
        return " ".join(ans)
            

        