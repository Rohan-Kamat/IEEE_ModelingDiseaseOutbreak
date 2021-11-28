def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1:
            return 1
        A = []
        for i in range(numCourses):
            A.append([])
        for i in prerequisites:
            A[i[0]].append(i[1])
        i = 0
        stack = [[0,0]]
        while i < len(A):
            x,y = stack[-1][0],stack[-1][1]
            if A[x] != -2 and y < len(A[x]):
                if A[x][y] >= 0:
                    temp = A[x][y]
                    A[x][y] = -1
                    stack.append([temp,0])
                else:
                    return 0
            else:
                stack.pop()
                A[x] = -2
                if len(stack) == 0:
                    i+=1
                    stack.append([i,0])
                else:
                    stack[-1][1] += 1
        return 1