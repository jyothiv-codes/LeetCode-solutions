class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(index,l):
            if len(l)==len(digits):
                answer.append("".join(l))
                return 
            curr_digit_mapping=mapping[digits[index]]
            for char in curr_digit_mapping:
                l.append(char)
                backtracking(index+1,l)
                l.pop()
        if len(digits)==0:
            return []
        mapping={}
        answer=[]
        mapping['2']=["a","b","c"]
        mapping['3']=["d","e","f"]
        mapping['4']=["g","h","i"]
        mapping['5']=["j","k","l"]
        mapping['6']=["m","n","o"]
        mapping['7']=["p","q","r","s"]
        mapping['8']=["t","u","v"]
        mapping['9']=["w","x","y","z"]
        backtracking(0,[])
        return answer
        

        