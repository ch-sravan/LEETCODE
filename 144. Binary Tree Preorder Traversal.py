# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(root,l):
        if(root==None):
            return 
        l.append(root.val)
        Solution.preorder(root.left,l)
        Solution.preorder(root.right,l)
        return l
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        Solution.preorder(root,l)
        return l
