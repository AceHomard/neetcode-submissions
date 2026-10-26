class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perim = 0
        directions = (1,0) , (-1,0) , (0,1) , (0,-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr,dc in directions:
                            nr, nc = r + dr, c + dc
                            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 0:
                                perim += 1
        return perim