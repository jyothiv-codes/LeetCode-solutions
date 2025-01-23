class Solution:
    def rob(self, nums: List[int]) -> int:
        #nums.append(0)
        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return max(nums[0],nums[1])
        
        nums1=nums[0:-1]
        dp1=[0]*len(nums1) #0 to n-2
        
        nums2=nums[1:]
        dp2=[0]*len(nums2) #1 to n-1
        dp1[0]=nums1[0]
        dp1[1]=max(nums1[0],nums1[1])
        dp2[0]=nums2[0]
        dp2[1]=max(nums2[0],nums2[1])
        print(nums1,nums2)
        for i in range(2,len(nums1)):
            
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums1[i])
        print(dp1)

        for i in range(2,len(nums2)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums2[i])
        print(dp2)

        return max(dp1[-1],dp2[-1])