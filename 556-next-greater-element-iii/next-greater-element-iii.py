class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = list(map(int, str(n)))
        l = len(num)
        i = l - 2
        while i >= 0 and num[i] >= num[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = l - 1
        while num[j] <= num[i]:
            j -= 1
    
        num[i], num[j] = num[j], num[i]
        num[i + 1:] = reversed(num[i + 1:])
        ans = int(''.join(map(str, num)))
        return ans if ans < 2**31 else -1