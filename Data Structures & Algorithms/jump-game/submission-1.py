class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
                if i == 0:
                    res = True
        return res    
            