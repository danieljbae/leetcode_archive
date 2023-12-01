# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case:
        if not root:
            return []


        # Use DFS create column_nodes map
        def dfs(node: Optional[TreeNode], col_num: int, row_num) -> None:
            if node:
                # Add node to map 
                column_nodes[col_num].append((node.val, row_num)) # col_num: [(node.val, row_num), ...]
                # Traverse 
                dfs(node.left, col_num-1, row_num+1)
                dfs(node.right, col_num+1, row_num+1)
        
        column_nodes = collections.defaultdict(list)
        dfs(node = root, col_num = 0, row_num = 0)

        # Then sort map by keys 
        sorted_keys = sorted(column_nodes.keys())

        # Loop through keys and append values to output 
        output = [] 
        for key in sorted_keys:
            # Sort nodes in a column by row 
            sorted_nodes = [val for val, row_num in sorted(column_nodes[key], key = lambda x : x[1])]
            output.append(sorted_nodes)

        return output