class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        possible_count=int(len(sequence)/len(word))+1
        flag=False
        count=0
        if word not in sequence:
            return 0
        while possible_count>0:
            s=word*possible_count
            print(s)
            if s in sequence:
                flag=True
                count=possible_count
                return count
            elif word in sequence:
                possible_count-=1  
        return count

        