class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # [1,1,2]
        # []
        # [1]... or [] at i=1, nums[1]==nums[0], need to skip and move to i=2
        # O(n * 2^n)
        res = []
        nums.sort()
        path = []

        def backtrack(start: int):
            res.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        
        backtrack(0)
        return res