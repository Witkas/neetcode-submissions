# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        def helper(pre, in_start, in_end):
            if not pre or in_start > in_end:
                return None
            root_val = pre[0]
            root = TreeNode(root_val)
            mid = inorder_index[root_val]
            left_size = mid - in_start
            root.left = helper(pre[1:1+left_size], in_start, mid-1)
            root.right = helper(pre[1+left_size:], mid+1, in_end)
            return root
        return helper(preorder, 0, len(inorder)-1)