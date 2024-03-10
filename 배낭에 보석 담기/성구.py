import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gems = []
for _ in range(N):
    gems.append(tuple(map(int, input().split())))

gems.sort(key=lambda x:(-x[1]/x[0]))
val = 0
i = 0
while M > 0 and i < N:
    if M >= gems[i][0]:
        val += gems[i][1]
        M -= gems[i][0]
    else:
        val += gems[i][1] * (M / gems[i][0])
        break
    i += 1

print(f"{val:.3f}")