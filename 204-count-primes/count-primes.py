class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        numbers=[True]*n
        numbers[0]=False
        numbers[1]=False
        for i in range(2,int(sqrt(n))+1):
            if numbers[i]:
                for multiple in range(i*i,n,i):
                    numbers[multiple]=False
        #print(numbers)
        return sum(numbers)
        