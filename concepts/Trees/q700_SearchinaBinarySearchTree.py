# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        
        Analysis: Iterative
        - Time: avg O(log n) w.c. O(n)
        - Space: avg O(log n) w.c. O(n)
        """
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right

        return None
    
    
    
    
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        Analysis: Iterative
        - Time: avg O(log n) w.c. O(n)
        - Space: avg O(log n) w.c. O(n)
        '''
        stack = [root]
        while stack:
            cursor = stack.pop()
            if cursor.val == val:
                return cursor
            if cursor.val > val:
                stack.append(cursor.left)
            else:
                stack.append(cursor.right)
        return None


    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        Analysis: Iterative constant space
        - Time: avg O(log n) w.c. O(n)
        - Space: O(1)
        '''
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root