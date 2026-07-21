class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}            
        for i, n in enumerate(nums):
            difference = target - n
            if difference in indexes:
                j = indexes[difference]
                if i != j:
                    return [min(i, j), max(i, j)]
            indexes[n] = i
