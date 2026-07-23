class Solution:
    # nums = [1,2,4,6]
    # prefix:
    # res = [1]
    # res = [1,1]
    # res = [1,1,2]
    # res = [1,1,2,8]
    # postfix:
    # res = [1,1,2,8]
    # res = [1,1,12,8]
    # res = [1,24,12,8]
    # res = [48,24,12,8]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[-1] * nums[i-1])
        multiplier = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= multiplier
            multiplier *= nums[i]
        return res
