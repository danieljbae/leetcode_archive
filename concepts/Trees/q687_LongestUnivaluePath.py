# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.longest = 0 # OOP: global variable to keep track of longest univalue path 
        self.dfs_post(root)
        return self.longest
    
    def dfs_post(self, node): # Left,Right,Data/return Node
        if not node: # invalid tree
            return None,0 
        
        if not node.left and not node.right: # Leaf node reached 
            return node.val, 1
        
        # recurse down - store: children val and the value's cumaltive count
        leftVal, Lcount = self.dfs_post(node.left) 
        rightVal, Rcount  = self.dfs_post(node.right)
        
        if node.val == leftVal and node.val == rightVal: # node (parent) has same value as left + right child
            self.longest = max(self.longest, Lcount + Rcount)
            return node.val, max(Lcount, Rcount) + 1 
        
        if node.val == leftVal: 
            self.longest = max(self.longest, Lcount) # update global max 
            return node.val, Lcount + 1 # return upwards node val and increase count for matching val
            
            
        if node.val == rightVal: 
            self.longest = max(self.longest, Rcount) 
            return node.val, Rcount + 1  #
            
        return node.val, 1 # add count of 1 for unique node
        
        