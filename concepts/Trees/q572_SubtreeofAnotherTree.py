# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """        
        
        # String representations of tree values, helper returns list of tree values
        s_Out_str = ''.join(map(str,self.helper_traverse(s))) # Join + Map, converts list into string
        t_Out_str = ''.join(map(str,self.helper_traverse(t)))
        
        if t_Out_str in s_Out_str: # string/set logic to check if we have exact subset
            return True
        else:
            return False 

    def helper_traverse(self,node):
        """
        Tree traversal function, returns a list of all node values
        """
        
        if node: # Recurse - if we have valid node, then use append node val (delim by "#") 
            return ['#', node.val] + self.helper_traverse(node.left) + self.helper_traverse(node.right)
        # otherwise we reach leaf/null node then append  "N"
        return ['n']
        