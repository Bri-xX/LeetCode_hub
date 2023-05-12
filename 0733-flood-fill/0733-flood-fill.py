class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        origin = image[sr][sc]
        def dfs(row: int, col: int):
            if row < 0 or row >= r or col < 0 or col >= c:
                return
            if image[row][col] == color or image[row][col] != origin:
                return
            else:
                image[row][col] = color
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)
        dfs(sr, sc)
        return image