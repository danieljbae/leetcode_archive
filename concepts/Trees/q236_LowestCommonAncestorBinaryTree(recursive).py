# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Analysis: recursive
        - Time: O(n)
        - Space: O(n)
        """
        
        # Base Case: End of branch 
        if root is None:
            return None
        
        # Base Case: Found node 
        if root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Both nodes found 
        if left and right:
            return root
        
        # Bubble up node that was found
        return left if right is None else right