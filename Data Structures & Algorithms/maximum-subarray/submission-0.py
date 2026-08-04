class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1e9
        curSum = -1e9
        for i in range(len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            res = max(curSum, res)
        return res