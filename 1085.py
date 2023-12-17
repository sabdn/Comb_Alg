inf = 0x1FFFFFFF
maxn = 100
maxk = 100
A = [[inf] * (maxn + 1) for _ in range(maxn + 1)]

class Friend:
    def __init__(self, home, cash, ticket):
        self.home = home
        self.cash = cash
        self.ticket = ticket

def cost(i, K):
    cost = 0
    for k in range(1, K + 1):
        h = friends[k].home
        if A[h][i] == inf:
            return -1
        elif friends[k].ticket:
            continue
        elif A[h][i] * 4 > friends[k].cash:
            return -1
        cost += A[h][i] * 4
    return cost

N, M = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        A[i][j] = 0 if i == j else inf

for _ in range(M):
    input_line = input().split()
    L = int(input_line[0])
    v = list(map(int, input_line[1:]))
    for i in range(L):
        for j in range(L):
            if v[i] != v[j]:
                A[v[i]][v[j]] = A[v[j]][v[i]] = 1

K = int(input())
friends = [Friend(0, 0, False) for _ in range(maxk + 1)]

for i in range(1, K + 1):
    input_line = input().split()
    cash, home, ticket = map(int, input_line)
    friends[i] = Friend(home, cash, ticket)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[i][j] = A[j][i] = min(A[i][j], A[i][k] + A[k][j])

mincost = inf
mins = 0

for i in range(1, N + 1):
    c = cost(i, K)
    if c != -1 and c < mincost:
        mins = i
        mincost = c

if mincost == inf:
    print(0)
else:
    print(mins, mincost)
