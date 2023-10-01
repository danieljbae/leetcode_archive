# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        
        Analysis: BFS with Queue
        - Time:
        - Space: 
        """
        if not root:
            return []
        
        
        que = [[root]]
        
        for level in que: # Traverse each Layer
            layer_nodes = []
            for node in level: # Traverse nodes within a layer
                
                if node.left:
                    layer_nodes.append(node.left)
                if node.right:
                    layer_nodes.append(node.right)
                
            if layer_nodes: # append to level grouped list, if nodes exist in a gievn layer 
                que.append(layer_nodes)
                
        vals = [[node.val for node in layer_nodes] for layer_nodes in que] # traverse layer and traverse each node in layer to convert to node's value
        return [sum(level)/float(len(level))  for level in vals]
        
        
                    
                
                
                
                
            
            
            
        
        
        