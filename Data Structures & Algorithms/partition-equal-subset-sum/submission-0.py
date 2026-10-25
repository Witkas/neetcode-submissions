class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        achievable = {0}
        for n in nums:
            new_sums = set(achievable)
            for s in achievable:
                new_sums.add(s + n)
                if s + n == target:
                    return True
            achievable = new_sums
        return False
