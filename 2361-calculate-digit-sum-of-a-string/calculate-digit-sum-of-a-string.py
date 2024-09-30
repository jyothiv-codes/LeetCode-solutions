class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            i=0
            temp_list=[]
            while i<len(s):
                if i+k<len(s):
                    temp_list.append(sum([int(x) for x in s[i:i+k]]))
                else:
                    temp_list.append(sum([int(x) for x in s[i:]]))
                i+=k
            print(temp_list)
            s="".join([str(x) for x in temp_list])
            print(s)
            
        return s

        