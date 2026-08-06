class Solution:
    # [0,1,4,7] target=10
    # [1,2,2,1]
    # (target-cars[0]) / cars[1]
    # 3turns
    # 4turns res += 1

    # cars = [(0,1),(1,2),(4,2),(7,1)]
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda c: c[0])
        turns = 0
        for i in range(len(cars) - 1, -1, -1):
            turns_needed = (target-cars[i][0]) / cars[i][1]
            if turns < turns_needed:
                res += 1
                turns = turns_needed
        return res
        