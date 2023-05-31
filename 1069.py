import heapq

maxn = 7500

input_list = []
freq = [0] * (maxn + 1)
v = [[] for _ in range(maxn + 1)]

N = 0
line = input()
numbers = line.split()
for number in numbers:
    x = int(number)
    input_list.append(x)
    freq[x] += 1
    N += 1

q = []
for i in range(1, N + 1):
    if freq[i] == 0:
        heapq.heappush(q, i)

for i in range(N):
    x = input_list[i]
    v[q[0]].append(x)
    v[x].append(q[0])
    heapq.heappop(q)
    if freq[x] > 0:
        freq[x] -= 1
    if freq[x] == 0:
        heapq.heappush(q, x)

for i in range(1, N + 2):
    print(f"{i}: ", end='')
    v[i].sort()
    for c in v[i]:
        print(c, end=' ')
    print()
