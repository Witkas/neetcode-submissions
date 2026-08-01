# heapq.heappush(list, val)
# heapq.heappop(list) <- pops the smallest

class MedianFinder:

    def __init__(self):
        # Both should be more or less equal size
        self.small = [] # MaxHeap (reversed Python's heapq)
        self.large = [] # MinHeap

    def addNum(self, num: int) -> None:
        if len(self.small) <= len(self.large):
            heapq.heappush(self.small, -1 * num)
        else:
            heapq.heappush(self.large, num)
        
        if self.small and self.large:
            if not (-1 * self.small[0]) <= self.large[0]:
                if len(self.small) == len(self.large):
                    a = -1 * heapq.heappop(self.small)
                    b = -1 * heapq.heappop(self.large)
                    heapq.heappush(self.small, b)
                    heapq.heappush(self.large, a)
                elif len(self.small) < len(self.large):
                    heapq.heappush(self.small, -1 * heapq.heappop(self.large))
                else:
                    heapq.heappush(self.large, -1 * heapq.heappop(self.small))

    def findMedian(self) -> float:
        if not self.small and not self.large:
            return None
        if len(self.small) == len(self.large):
            return (-1 * (self.small[0]) + self.large[0]) / 2
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return -1 * self.small[0]
        