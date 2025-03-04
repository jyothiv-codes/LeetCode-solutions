from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_odd_inc(self,nums):
        if len(nums)>1:
            for i in range(1,len(nums)):
                if nums[i]>nums[i-1] and (nums[i]%2!=0 and nums[i-1]%2!=0):
                    pass
                else:
                    return False
            return True
        else:
            if nums[0]%2!=0:
                return True
            return False
    def check_even_dec(self,nums):
        if len(nums)>1:
            for i in range(1,len(nums)):
                if (nums[i]<nums[i-1]) and (nums[i]%2==0 and nums[i-1]%2==0):
                    pass
                else:
                    return False
            return True
        else:
            if nums[0]%2==0:
                return True
            return False
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # let's do a level order traversal to store elements at each level
        answer=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            temp=[]
            for i in range(n):
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(temp)
        print(answer)
        for i in range(len(answer)):
            if i==0:
                if answer[i][0]%2!=0:
                    pass
                else:
                    return False
            elif i%2==0:
                if not self.check_odd_inc(answer[i]):
                    return False
            else:
                if not self.check_even_dec(answer[i]):
                    return False
        return True
    
    


        

        