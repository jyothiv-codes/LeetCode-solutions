class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score=0
        a, b, c = sorted([a,b,c])
        while (a>0 and b>0) or (c>0 and b>0) or (a>0 and c>0):
            a, b, c = sorted([a,b,c])
            if (a>0 and c>0):
                a-=1
                c-=1
            elif (a>0 and b>0):
                a-=1
                b-=1
            elif (c>0 and b>0):
                c-=1
                b-=1
            
            score+=1
            print(a,b,c)
        print(a,b,c)
        print(score)
        return score

        