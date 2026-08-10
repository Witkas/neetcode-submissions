class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0

        for num in nums:
            left, right = right, max(right, num + left)
        return right