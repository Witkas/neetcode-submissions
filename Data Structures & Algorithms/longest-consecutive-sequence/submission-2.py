class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        neg, zeroAndPos = [0] * (abs(min(nums)) + 1), [0] * (max(nums) + 1)
        for n in nums:
            if n < 0:
                neg[abs(n)] += 1
            else:
                zeroAndPos[n] += 1
        # Combine
        combined = []
        for i in range(len(neg)-1, 0, -1):
            combined.append(neg[i])
        for i in range(len(zeroAndPos)):
            combined.append(zeroAndPos[i])
        # Count
        res = 0
        temp = 0
        for i, n in enumerate(combined):
            if n > 0:
                temp += 1
            if n == 0 or i == len(combined) - 1:
                res = max(res, temp)
                temp = 0
        return res
