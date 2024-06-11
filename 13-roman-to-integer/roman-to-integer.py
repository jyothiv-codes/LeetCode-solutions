class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer=0
        prev=""
        for ch in s:
            if ch=="M":
                if prev=="C":
                    answer+=900
                    answer-=100
                else:
                    answer+=1000
            elif ch=="D":
                if prev=="C":
                    answer+=400
                    answer-=100
                else:
                    answer+=500
            elif ch=="C":
                if prev=="X":
                    answer+=90
                    answer-=10
                else:
                    answer+=100
            elif ch=="L":
                if prev=="X":
                    answer+=40
                    answer-=10
                else:
                    answer+=50
            elif ch=="X":
                if prev=="I":
                    answer+=9
                    answer-=1
                else:
                    answer+=10
            elif ch=="V":
                if prev=="I":
                    answer+=4
                    answer-=1
                else:
                    answer+=5
            elif ch=="I":
                answer+=1
            prev=ch
        return answer
        