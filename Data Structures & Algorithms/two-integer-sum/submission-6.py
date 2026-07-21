class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}            
        for j, n in enumerate(nums):
            difference = target - n
            if difference in indexes:
                i = indexes[difference]
                return [i, j]
            indexes[n] = j
