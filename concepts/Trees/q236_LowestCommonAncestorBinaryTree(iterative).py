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
        
        Analysis: Iterative, stack and hashmap
        - Time: O(n)
        - Space: O(n) w/ hashmap + stack; w.c. p and q are leaf nodes
        """
        parent = {root:None} # Parent hashmap to backtrack LCA 
        stack = [root]
        
        # Traverse w/ stack
        while p not in parent or q not in parent:  # stop when both p and q in parent map, as we can start backtracking
            cursor = stack.pop()
            
            if cursor.left:
                stack.append(cursor.left)
                parent[cursor.left] = cursor    
            if cursor.right:
                stack.append(cursor.right)
                parent[cursor.right] = cursor
        
        # Backtrack p and q paths to find LCA
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q 
            
            
            
            