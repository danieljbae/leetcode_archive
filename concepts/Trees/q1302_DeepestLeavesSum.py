# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # deepest_layer = 0
    
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        layer_map = {}
        layer = 0
        self.dfs(root,layer_map,layer)
        print(layer_map)
        return layer_map[max(layer_map)]
    
    def dfs(self, root, layer_map,layer):
        
        if root:
            if root.left:
                self.dfs(root.left, layer_map,layer+1)
            if root.right:
                self.dfs(root.right, layer_map,layer+1)
        
        if layer in layer_map:
            layer_map[layer] += root.val
        else:
            layer_map[layer] = root.val