def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        queue = []
        A = [0]*n
        count = 0
        index = 0
        i = 0
        while index < n:
            if len(queue) == 0:
                if A[index] == 0:
                    count += 1
                    A[index] = count
                    for j in range(index + 1,n):
                        if isConnected[index][j] == 1:
                            queue.append(j)
                            A[j] = count
                index += 1
            else:
                i = queue.pop(0)
                for j in range(index,n):
                    if isConnected[i][j] == 1 and A[j] == 0:
                        queue.append(j)
                        A[j] = count
        return count