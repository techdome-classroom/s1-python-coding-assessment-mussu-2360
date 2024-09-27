class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Helper function to perform Depth-First Search (DFS)
        def dfs(r, c):
            # Base case: Stop DFS if out of bounds or at water ('W')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return

            # Mark the current landmass ('L') as visited by setting it to 'W'
            grid[r][c] = 'W'

            # Explore all four possible directions: up, down, left, right
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        island_count = 0

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find a landmass ('L'), start DFS
                if grid[r][c] == 'L':
                    island_count += 1
                    dfs(r, c)  # Perform DFS to mark the entire island

        return island_count


# Test cases
solution = Solution()

grid1 = [["L", "L", "L", "L", "W"], 
         ["L", "L", "W", "L", "W"], 
         ["L", "L", "W", "W", "W"], 
         ["W", "W", "W", "W", "W"]]
print(solution.getTotalIsles(grid1))  # Output: 1

grid2 = [["L", "L", "W", "W", "W"], 
         ["L", "L", "W", "W", "W"], 
         ["W", "W", "L", "W", "W"], 
         ["W", "W", "W", "L", "L"]]
print(solution.getTotalIsles(grid2))  # Output: 3

