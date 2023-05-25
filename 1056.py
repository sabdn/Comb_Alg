class Node:
    def __init__(self):
        self.p = None
        self.v = []
        self.d = 0
        self.visited = 0


nodes = [Node() for _ in range(10001)]

n = int(input())

for i in range(2, n + 1):
    x = int(input())
    nodes[x].v.append(nodes[i])
    nodes[i].v.append(nodes[x])

maxnode = None
max_distance = 0
s = []
s.append(nodes[1])
nodes[1].visited = 1

while s:
    node = s.pop()
    if node.d > max_distance:
        max_distance = node.d
        maxnode = node

    for n in node.v:
        if not n.visited:
            n.visited = 1
            s.append(n)
            n.d = node.d + 1

s = []
s.append(maxnode)
maxnode.visited = 2
maxnode.d = 0
max_distance = -1

while s:
    node = s.pop()
    if node.d > max_distance:
        max_distance = node.d
        maxnode = node

    for n in node.v:
        if n.visited != 2:
            n.visited = 2
            s.append(n)
            n.d = node.d + 1
            n.p = node

ans = []
node = maxnode

while node:
    if maxnode.d // 2 == node.d or maxnode.d // 2 + maxnode.d % 2 == node.d:
        ans.append(nodes.index(node))
    node = node.p

ans.sort()

for a in ans:
    print(a, end=' ')
