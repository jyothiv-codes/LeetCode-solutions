class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output=[]
        for word in words:
            temp_list=[ch for ch in chars]
            flag=True
            for ch in word:
                if ch in temp_list:
                    temp_list.remove(ch)
                else:
                    flag=False
                    break
            if flag==True:
                output.append(word)
        sum_=0
        for word in output:
            sum_+=len(word)
        return sum_

                
        