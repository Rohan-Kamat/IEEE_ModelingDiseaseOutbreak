def root(a):
    while V[a - 1] != a:
        V[a - 1] = V[V[a - 1] - 1]
        a = V[a - 1]
    return a


def union(a,b):
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return 0
    elif size[ra - 1] >= size[rb - 1]:
        V[rb - 1] = V[ra - 1]
        size[ra - 1] += size[rb - 1]
    else:
        V[ra - 1] = V[rb - 1]
        size[rb - 1] += size[ra - 1]
    return 1


def merge_sort(A,l,u):
    if l >= u:
        return 
    mid = (u + l)//2
    merge_sort(A,l,mid)
    merge_sort(A,mid + 1,u)
    a,b = l,mid + 1
    while a <= mid and b <= u:
        if A[b][2] < A[a][2]:
            x = A.pop(b)
            A.insert(a,x)
            a += 1
            b += 1
            mid += 1
        else:
            a += 1


V = []
E = []
size = []

s = input()
s = s.split()
N,M = int(s[0]),int(s[1])
for i in range(1,N + 1):
    V.append(i)
    size.append(1)
for i in range(M):
    s = input()
    s = s.split()
    E.append([int(s[0]),int(s[1]),int(s[2])])
merge_sort(E,0,M - 1)
sum = 0
for i in E:
    if union(i[0],i[1]):
        sum += i[2]
print(sum)
