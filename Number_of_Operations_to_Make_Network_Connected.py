def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        A = [0]*n # Stores the component number of each node
        N = [] # stores neighbours of each node
        for i in range(n):
            N.append([])
        for i in connections:
            N[i[0]].append(i[1])
            N[i[1]].append(i[0])
        #N : ith array has all neighbours of ith node
        count = 0
        extra = 0
        stack = []
        # Applying DFS
        i = j = 0
        index = 0
        while index < n:
            if len(stack) == 0:
                if A[index] == 0:
                    count += 1
                    stack.append([index,0])
                    A[index] = count
                index += 1
            else:
                i,j = stack[-1][0],stack[-1][1]
                if j >= len(N[i]):
                    stack.pop()
                    if stack:
                        stack[-1][1] += 1
                else:
                    if A[N[i][j]] == 0:
                        stack.append([N[i][j],0])
                        A[N[i][j]] = count
                    elif A[N[i][j]] == count:
                        if N[i][j] != stack[-2][0]:#Checking for existence of a cycle
                            extra += 1
                            N[N[i][j]].remove(i)
                        stack[-1][1] += 1
        if extra >= count - 1:
            return count - 1
        else:
            return -1