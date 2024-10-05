class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0]!=s2[0] or s2[0]!=s3[0]:
            return -1
        if s1==s2==s3:
            return 0
        strings = [s1, s2, s3]
        count=0
        strings_sorted = sorted(strings, key=len)
        s1,s2,s3=strings_sorted
        while len(s3)>0:
            l=[ch for ch in s3]
            l=l[:-1]
            s3="".join(l)
            count+=1
            print(s1,s2,s3)
            if s1==s2==s3:
                return count
            strings = [s1, s2, s3]
            strings_sorted = sorted(strings, key=len)
            s1,s2,s3=strings_sorted
        return -1
                