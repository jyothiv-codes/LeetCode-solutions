# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def formTree(nums,start,end):
            if start<=end:
                mid=(start+end)//2
                print("mid",mid)
                node=TreeNode(nums[mid])
                print(node)
                print("start,mid-1",start,mid-1)
                print("mid+1,end",mid+1,end)
                node.left=formTree(nums,start,mid-1)
                node.right=formTree(nums,mid+1,end)
                
                return node
        return formTree(nums,0,len(nums)-1)

        