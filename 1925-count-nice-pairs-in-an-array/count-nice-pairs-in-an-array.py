class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def calc_rev(n):
            return int(str(n)[::-1])
        arr=[]
        # calc revs
        total=0
        for i in range(len(nums)):
            arr.append(nums[i]-calc_rev(nums[i]))
        ans=0
        mod=10**9+7
        dic = defaultdict(int)
        for num in arr:
            ans=(ans+dic[num])%mod
            dic[num]+=1
        print(dic)
        return ans

        