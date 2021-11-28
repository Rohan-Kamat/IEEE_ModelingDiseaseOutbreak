 def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def root(a):
            while (Arr[a - 1] != a):
                Arr[a - 1] = Arr[Arr[a - 1] - 1]
                a = Arr[a - 1]
            return a


        Arr = []
        size = []
        n = len(edges)
        for i in range(1, n + 1):
            Arr.append(i)
            size.append(1)
        edge = []
        for i in edges:
            a, b = i[0], i[1]
            ra,rb = root(a),root(b)
            if ra == rb:
                edge = i
            elif size[ra - 1] >= size[rb - 1]:
                Arr[rb - 1] = Arr[ra - 1]
                size[ra - 1] += size[rb - 1]
            else:
                Arr[ra - 1] = Arr[rb - 1]
                size[rb - 1] += size[ra - 1]
        return edge
        