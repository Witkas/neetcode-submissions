# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.res
    # def maxWithSplit(self, root):
    #     maxLeft, maxRight = 0, 0
    #     if root.left:
    #         maxLeft = self.maxNoSplit(root.left)
    #     if root.right:
    #         maxRight = self.maxNoSplit(root.right)
    #     return max(root.val, root.val + maxLeft, root.val + maxRight, root.val + maxLeft + maxRight)
    
    # def maxNoSplit(self, root):
    #     maxLeft, maxRight = 0, 0
    #     if root.left:
    #         maxLeft = self.maxNoSplit(root.left)
    #     if root.right:
    #         maxRight = self.maxNoSplit(root.right)
    #     return max(0, root.val, root.val + maxLeft, root.val + maxRight)