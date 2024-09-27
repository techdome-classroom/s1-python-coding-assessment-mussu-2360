class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            
            grid[r][c] = 'W'
           
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        island_count = 0

     
        for r in range(rows):
            for c in range(cols):
              
                if grid[r][c] == 'L':
                    island_count += 1
                    dfs(r, c)  

        return island_count


solution = Solution()

grid1 = [["L", "L", "L", "L", "W"], ["L", "L", "W", "L", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "W", "W", "W"]]
print(solution.getTotalIsles(grid1))  # Output: 1


grid2 = [["L", "L", "W", "W", "W"], ["L", "L", "W", "W", "W"], ["W", "W", "L", "W", "W"], ["W", "W", "W", "L", "L"]]
print(solution.getTotalIsles(grid2))  # Output: 3

print(numIslands(grid1))  # Output: 1


grid2 = [["L","L","W","W","W"], ["L","L","W","W","W"], ["W","W","L","W","W"], ["W","W","W","L","L"]]
print(numIslands(grid2))  # Output: 3
