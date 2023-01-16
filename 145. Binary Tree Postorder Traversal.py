# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(root,l):
        if(root==None):
            return None
        Solution.postorder(root.left,l)
        Solution.postorder(root.right,l)
        l.append(root.val)
        return l
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        Solution.postorder(root,l)
        return l
