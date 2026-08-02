class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxi, mini = 1, 1
        for n in nums:
            tmp = maxi * n
            maxi = max(maxi * n, mini * n, n)
            mini = min(tmp, mini * n, n)
            res = max(res, maxi)
        
        return res