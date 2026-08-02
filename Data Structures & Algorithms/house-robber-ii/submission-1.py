class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_support(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)
            return rob2
        if len(nums) == 1:
            return nums[0]
        return max(rob_support(nums[:len(nums)-1]), rob_support(nums[1:]))
        