class Gear:
    def __init__(self):
        self.adj = []
        self.cogs = 0
        self.visited = False
        self.parity = False


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def dfs(start, gears):
    stack = [start]
    gears[start].visited = True

    while stack:
        current = stack.pop()
        for v in gears[current].adj:
            if not v.visited:
                v.parity = not gears[current].parity
                v.visited = True
                stack.append(gears.index(v))


def main():
    N = int(input())
    gears = [Gear() for _ in range(N + 1)]

    for i in range(1, N + 1):
        gear_info = list(map(int, input().split()))
        gears[i].cogs = gear_info[0]
        for x in gear_info[1:]:
            if not x:
                break
            gears[i].adj.append(gears[x])

    start, V = map(int, input().split())
    V *= gears[start].cogs
    if V < 0:
        V = -V
        gears[start].parity = True
    dfs(start, gears)

    for i in range(1, N + 1):
        if not gears[i].visited:
            print("0/1")
        else:
            g = gcd(gears[i].cogs, V)
            sign = "-" if gears[i].parity else ""
            print(f"{sign}{V // g}/{gears[i].cogs // g}")


if __name__ == "__main__":
    main()
