class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        rows = len(image)
        cols = len(image[0])
        image[sr][sc] = color
        file = deque([(sr, sc)])
        while file:
            r, c = file.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    image[nr][nc] = color
                    file.append((nr,nc))
        return image