# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = [root.val]
        l = []
        
        def left(node):
            if node.left or node.right:  
                ans.append(node.val)
                if node.left:
                    left(node.left)
                elif node.right:
                    left(node.right)

        def right(node):
            if node.left or node.right:  
                l.append(node.val)
                if node.right:
                    right(node.right)
                elif node.left:
                    right(node.left)
            
        def child(node):
            if node.left:
                child(node.left)
            if node.right:
                child(node.right)
            if not node.left and not node.right:
                ans.append(node.val)

                
            
        if root.left:
            left(root.left)
            child(root.left)
        if root.right:
            right(root.right)
            child(root.right)
        
        return ans + l[::-1]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            