class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        l = [[] for _ in range(len(nums) + 1)]
        for n, count in counter.items():
            l[count].append(n)
        
        res = []
        for i in range(len(l) - 1, 0, -1):
            res.extend(l[i])
            if len(res) == k:
                return res
