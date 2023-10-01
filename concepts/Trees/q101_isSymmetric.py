# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Analysis: Recurisve 
        - Time: O(n)
        - Space: O(n) n recursive stacks
        """
        if not root:
            return True     
        
        def helper(leftNode, rightNode):
            """
            Checks 2 subtrees symmetry
            Recurses with mirror children on BOTH subtrees
            """
            # Base case: Ensure if one root is Null, other is Null  
            if not leftNode or not rightNode:
                return leftNode == rightNode 

            # Base case: 2 valid subtree roots, if both are equal
            if leftNode.val != rightNode.val:
                return False

            # recurse in mirror fasion 
            return helper(leftNode.left,rightNode.right) and helper(leftNode.right,rightNode.left) 
        
        return helper(root.left, root.right)



"""
Base Cases:

If both subtrees root nodes are Null, continue exploring (as we do not know if Tree is symmetric or not yet)
If only one of the subtree root nodes are Null then return False
If both root nodes are valid and not equal, return False

"""
        
        