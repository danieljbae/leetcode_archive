# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        
        Analysis: Divide and Conquer // Decrease and Conquer
        - Time: O(n) visit every node
        - Space: O(n) recursion stacks
        """            
        if root is None:
            return None

        elif root.val > high: # exeeds ceiling
            return self.trimBST(root.left, low, high) # trim and look for smaller 

        elif root.val < low: # exceeds floor
            return self.trimBST(root.right, low, high) # look for bigger

        # node is within bounds, so build new tree
        else:
            # returns of recursive calls trims tree
            root.left = self.trimBST(root.left, low, high)  
            root.right = self.trimBST(root.right, low, high) 
            return root

        
            