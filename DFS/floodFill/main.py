class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        similar_color = image[sr][sc]
        if similar_color == color:
            return image
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m = len(image)
        n = len(image[0])

        def checkBondareis(row,col):
            return row < m and row >=0 and col < n and col >=0 
        def dfs(row,col):
            if not checkBondareis(row,col) or image[row][col] != similar_color:
                return
            # Flood fill
            image[row][col] = color
            for rd,cd in directions:
                dfs(row+rd,col+cd)
            
        dfs(sr,sc)
        return image
        

