from collections import deque


class Node:
    def __init__(self):
        self.d = maxn
        self.x = 0
        self.y = 0
        self.p = None
        self.v = []


maxn = 1000

N = int(input())
input_data = []
nodes = [Node() for _ in range(maxn + 2)]
routes = [[] for _ in range(2001)]

for i in range(1, N + 1):
    x, y = map(int, input().split())
    input_data.append((x, y))
    nodes[i].x = x
    nodes[i].y = y
    routes[x].append(nodes[i])
    nodes[i].d = maxn

for i in range(1, N + 1):
    for r in routes[input_data[i - 1][1]]:
        nodes[i].v.append(r)
    for r in routes[input_data[i - 1][0]]:
        if r != nodes[i]:
            nodes[i].v.append(r)

r, x, y = map(int, input().split())
for r_node in routes[x]:
    nodes[N + 1].v.append(r_node)
for r_node in routes[y]:
    nodes[N + 1].v.append(r_node)

q = deque()
q.append(nodes[N + 1])
nodes[N + 1].d = 0

while q:
    node = q.popleft()

    if node.x == r or node.y == r:
        output = []
        while node != nodes[N + 1]:
            output.append(node)
            node = node.p
        output.reverse()
        print(len(output))
        for node in output:
            print(nodes.index(node))
        break

    for n in node.v:
        if n.d > node.d + 1:
            n.d = node.d + 1
            n.p = node
            q.append(n)
else:
    print("IMPOSSIBLE")
