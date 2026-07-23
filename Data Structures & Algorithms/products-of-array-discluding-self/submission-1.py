class Solution:

    # [1,2,4,6]
    # prefix = [1,1,2,8]
    # suffix = [48,24,6,1]
    # [48,24,12,8]

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        res = []
        for i in range(0, len(nums)-1):
            prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            suffix = [suffix[0] * nums[i]] + suffix
        for i in range(len(suffix)):
            res.append(suffix[i] * prefix[i])
        return res
        