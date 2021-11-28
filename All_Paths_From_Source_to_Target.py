 def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        node = []
        index = []
        n = len(graph)
        i = 0
        ans = []
        while 1:
            node.append(i)
            index.append(0)
            if i == n - 1:
                ans.append(list(node))
                node.pop()
                index.pop()
            while len(node) and (index[-1] >= len(graph[node[-1]]) - 1 ):
                node.pop()
                index.pop()
            if len(node) == 0:
                break
            i = graph[node[-1]][index[-1]]
        return ans