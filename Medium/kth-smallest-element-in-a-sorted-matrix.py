from heapq import heappop, heappush

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        f = [(matrix[0][0], 0, 0)]
        saw = set()
        cnt = 0
        while cnt < k:
            e, i, j = heappop(f)
            cnt += 1
            if i + 1 < len(matrix) and (i+1, j) not in saw:
                saw.add((i+1, j))
                heappush(f, (matrix[i+1][j], i+1, j))
            
            if j + 1 < len(matrix) and (i, j+1) not in saw:
                saw.add((i, j+1))
                heappush(f, (matrix[i][j+1], i, j+1))

        return e

            



            




