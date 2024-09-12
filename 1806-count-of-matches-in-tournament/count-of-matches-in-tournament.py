class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        while n>0:
            print(n)
            matches+=int(n/2)
            if n%2!=0:
                matches+=1                
            n=int(n/2)
            print("matches",matches)
        return matches-1
            

        