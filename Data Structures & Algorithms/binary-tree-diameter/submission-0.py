# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxSplit = 0
        def dfs(node):
            if not node.left and not node.right:
                return 0
            elif node.left and not node.right:
                return 1 + dfs(node.left)
            elif node.right and not node.left:
                return 1 + dfs(node.right)
            else:
                nonlocal maxSplit
                maxSplit = max(maxSplit, 2 + dfs(node.left) + dfs(node.right))
                return max(1 + dfs(node.left), 1 + dfs(node.right))
        maxSingle = dfs(root)
        return max(maxSingle, maxSplit)