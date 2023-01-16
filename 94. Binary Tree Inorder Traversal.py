# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(root,l):
        if(root==None):
            return None
        Solution.inorder(root.left,l)
        l.append(root.val)
        Solution.inorder(root.right,l)
        return l
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        Solution.inorder(root,l)
        return l
