# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructBST(nums,start,end):
            if start<=end:
                mid=(start+end)//2
                node=TreeNode(nums[mid])
                node.left=constructBST(nums,start,mid-1)
                node.right=constructBST(nums,mid+1,end)
                print(node)
                return node
        return constructBST(nums,0,len(nums)-1)
        