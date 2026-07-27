class Solution:
    # [3,3,4,5,6,1,2,3]
    # [3,3,3,4,1,3,3,3]
    # [1]
    # [2,1]
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                r = m - 1
        return res
