class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        res = 0
        visited = [[False] * ncol for _ in range (nrow)]

        def dfs(r, c) -> int:

            if r < 0 or r >= nrow or c < 0 or c >= ncol:
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0

            visited[r][c] = True # Mark as visited

            area = 1
            area += dfs(r, c - 1) # Left
            area += dfs(r, c + 1) # Right
            area += dfs(r - 1, c) # Up
            area += dfs(r + 1, c) # Down

            return area

        for r in range(nrow):
            for c in range(ncol):
                curArea = dfs(r, c)
                res = max(res, curArea)

        return res
