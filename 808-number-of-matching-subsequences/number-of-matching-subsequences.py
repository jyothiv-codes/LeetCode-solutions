class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count=0
        already_match=[]
        def check_subseq(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        for word in words:
            if check_subseq(word):
                count+=1

        return count
            

        