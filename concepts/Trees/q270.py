class Solution:
    def closestValue(self, root: TreeNode, target: float, min_diff=math.inf) -> int:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            
            if abs(node.val - target) < self.min_diff:
                self.result = node.val
                self.min_diff = abs(node.val - target)

            dfs(node.right)

        
        self.result = None
        self.min_diff = math.inf        
        dfs(root)
        
        return self.result