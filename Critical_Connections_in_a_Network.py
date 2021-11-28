def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        N = []
        arr = []
        for i in range(n):
            N.append([])
            arr.append(0)
        for i in connections:
            N[i[0]].append(i[1])
            N[i[1]].append(i[0])

        #DFS
        index = 0
        stack = [[0,0]]
        arr[0] = 1
        edges = []
        while stack:
            a,b = stack[-1][0],stack[-1][1]
            L = len(N[a])
            if b >= L:
                if edges and edges[index - 1][1] == a:
                    index -= 1
                stack.pop()
                if stack:
                    stack[-1][1] += 1
            else:
                if arr[N[a][b]] == 0:
                    stack.append([N[a][b],0])
                    arr[N[a][b]] = 1
                    edges.insert(index,[a,N[a][b]])
                    index += 1
                elif arr[N[a][b]] == 1:
                    if N[a][b] != stack[-2][0]:
                        i = -1
                        index -= 1
                        while stack[i][0] != N[a][b]:
                            if len(edges) == 0:
                                break
                            if edges[index][1] == stack[i][0]:
                                edges.pop(index)
                                index -= 1
                            i -= 1
                        index += 1
                        N[N[a][b]].remove(a)
                    stack[-1][1] += 1
        return edges