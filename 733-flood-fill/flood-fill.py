from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        queue=deque([[sr,sc]])
        visited=[]
        nr,nc=len(image),len(image[0])
        curr=image[sr][sc]
        while len(queue)>0:
            print(queue)
            pair=queue.popleft()
            r,c=pair[0],pair[1]
            visited.append(pair)
            image[r][c]=color
            #left 
            if c-1>=0 and image[r][c-1]==curr and image[r][c-1]!=color and [r,c-1] not in visited:
                queue.append([r,c-1])

            #right 
            if c+1<=nc-1 and image[r][c+1]==curr and image[r][c+1]!=color and [r,c+1] not in visited:
                queue.append([r,c+1])

            #up 
            if r-1>=0 and image[r-1][c]==curr and image[r-1][c]!=color and [r-1,c] not in visited:
                queue.append([r-1,c])

            #down
            if r+1<=nr-1 and image[r+1][c]==curr and image[r+1][c]!=color and [r+1,c] not in visited:
                queue.append([r+1,c])
        return image

        