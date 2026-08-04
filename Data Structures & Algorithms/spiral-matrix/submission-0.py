class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, l, r, b = 0, 0, len(matrix[0]), len(matrix)
        res = []

        while l < r and t < b:
            prevLeft, prevTop = l - 1, t - 1

            # Go left
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            # Go down
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            # Go left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            # Go top
            for i in range(b -  1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
    
        return res        
            