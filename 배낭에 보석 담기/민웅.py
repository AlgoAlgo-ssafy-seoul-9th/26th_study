import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

jewelys = []
for _ in range(N):
    w, v = map(int, input().split())

    jewelys.append([v/w, w, v])

jewelys.sort(key=lambda x: x[0])
# print(jewelys)

now_W = 0
ans = 0
while jewelys:
    value, W, total = jewelys.pop()
    if now_W + W <= M:
        ans += total
        now_W += W
    else:
        tmp = value*(M-now_W)
        ans += tmp
        break

print(format(round(ans, 3), '.3f'))