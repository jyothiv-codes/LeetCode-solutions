class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income==0:
            return 0
        index=0
        tax=0
        while income>0:
            upper,percent=brackets[index][0],brackets[index][1]
            print(upper,percent)
            if index==0:
                if upper<=income:
                    income-=upper
                    differ=upper
                else:
                    differ=income
                    income=0
            else:
                if upper-brackets[index-1][0]<=income:
                    income-=(upper-brackets[index-1][0])
                    differ=upper-brackets[index-1][0]
                else:
                    differ=income
                    income=0

            print("differ",differ)
            differ*=(brackets[index][1]/100)
            tax+=differ
            print(differ,tax)
            index+=1
        return tax


        