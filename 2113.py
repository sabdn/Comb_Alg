from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Node:
    def __init__(self):
        self.h = 0
        self.v = 0


class Pos:
    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r

    def __add__(self, other):
        return Pos(self.x + other[0], self.y + other[1], self.r)


def solve(k):
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            nodes[x][y].v = 0

    Qr = deque([Pos(r.x, r.y, r.r), Pos(w.x, w.y, w.r)])
    nodes[r.x][r.y].v = 2
    nodes[w.x][w.y].v = 1

    while Qr:
        p = Qr.popleft()
        cur_node = nodes[p.x][p.y]

        if p.r == 2 and cur_node.v == 1:
            continue

        for d in dirs:
            p2 = p + d
            next_node = nodes[p2.x][p2.y]

            if next_node.v == 1 or (p.r == 1 and next_node.h > cur_node.h) or (
                    p.r == 2 and (next_node.v == 2 or next_node.h - cur_node.h > k)):
                continue

            next_node.v = p.r
            Qr.append(p2)

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if nodes[x][y].v == 2:
                return True

    return False


def binary():
    L, R = 0, int(1e5) + 1

    while R - L > 0:
        m = (R + L) // 2
        if solve(m):
            R = m
        else:
            L = m + 1

    return L


if __name__ == "__main__":
    n, m = map(int, input().split())
    nodes = [[Node() for _ in range(n + 2)] for _ in range(m + 2)]

    for y in range(1, n + 1):
        for x, val in enumerate(map(int, input().split()), start=1):
            nodes[x][y].h = val

    for x in range(m + 2):
        for y in range(n + 2):
            nodes[x][y].v = 1

    r_y, r_x = map(int, input().split())
    w_y, w_x = map(int, input().split())
    r = Pos(r_x, r_y, 2)
    w = Pos(w_x, w_y, 1)

    res = binary()
    print(res if res <= int(1e5) else -1)
