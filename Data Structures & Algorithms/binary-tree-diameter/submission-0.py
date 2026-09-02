# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def helper(root):
            nonlocal dia
            if root == None:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            dia = max(dia,l+r)
            return max(l,r)+1

        helper(root)
        return dia














