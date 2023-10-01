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
        
        # End of branch 
        if root is None:
            return False
        
        # Node found, Return "not Null" to perculate
        if root is p or root is q:
            return True
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # both nodes are contained in same subtree 
        if left == True and right == True: 
            return root
        
        # both nodes not contained in same subtree
        if left == False and right == False:
            return False
        
        # perculate up tree
        return right if (left == False) else left