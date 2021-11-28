def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        l = len(queue)
        sum = 0
        i = 0
        time = 0
        if l == 0:
            if fresh == 0:
                return 0
            else:
                return -1
        while 1:
            x,y = queue[i][0],queue[i][1]
            if x != 0 and grid[x - 1][y] == 1:
                sum+=1
                queue.append((x - 1,y))
                grid[x - 1][y] = 2
                fresh -= 1
            if y != n - 1 and grid[x][y + 1] == 1:
                sum+=1
                queue.append((x,y + 1))
                grid[x][y + 1] =2
                fresh -= 1
            if x != m - 1 and grid[x + 1][y] == 1:
                sum+=1
                queue.append((x + 1,y))
                grid[x + 1][y] = 2
                fresh -= 1
            if y != 0 and  grid[x][y - 1] == 1:
                sum+=1
                queue.append((x,y - 1))
                grid[x][y - 1] = 2
                fresh -= 1
            i+=1
            if i == l:
                if sum != 0:
                    l += sum
                    sum = 0
                    time += 1
                else:
                    break
        if fresh == 0:
            return time
        else:
            return -1