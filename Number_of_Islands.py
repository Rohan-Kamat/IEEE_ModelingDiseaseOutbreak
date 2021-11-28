def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        m = len(grid)
        n = len(grid[0])
        index = 0
        i = j = 0
        count = 0
        while index < m*n:
            if len(queue) == 0:
                if grid[i][j] == '1':
                    count += 1
                    queue.append([i,j])
                    grid[i][j] = '2'
                else:
                    index += 1
                    i = index//n
                    j = index%n
            else:
                i,j = queue[0][0],queue[0][1]
                queue.pop(0)
                if i != m - 1 and grid[i + 1][j] == '1':
                    queue.append([i + 1,j])
                    grid[i + 1][j] = '2'
                if j != n - 1 and grid[i][j + 1] == '1':
                    queue.append([i,j + 1])
                    grid[i][j + 1] = '2'
                if i != 0 and  grid[i - 1][j] == '1':
                    queue.append([i - 1,j])
                    grid[i - 1][j] = '2'
                if j != 0 and grid[i][j - 1] == '1':
                    queue.append([i,j - 1])
                    grid[i][j - 1] = '2'
        return count