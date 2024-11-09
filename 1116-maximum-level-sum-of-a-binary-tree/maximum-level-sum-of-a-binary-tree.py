# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_max=0
        node=root
        queue=[]
        queue.append([node,1])
        level=1
        level_sum=[]
        while queue:
            node,level=queue.pop(0)
            if len(level_sum)>=level:
                level_sum[level-1]+=node.val
            else:
                level_sum.append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
        print(level_sum)
        return level_sum.index(max(level_sum))+1



