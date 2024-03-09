import sys

input = sys.stdin.readline
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
X, Y = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]
visited = [[[] for _ in range(N)] for _ in range(N)]

X = X - 1
Y = Y - 1

d = 0
ans = False
cnt = 0
visited[X][Y].append(d)
pos = [(X, Y)]
while pos:
    x, y = pos.pop()

    nx = x + dxy[d][0]
    ny = y + dxy[d][1]

    if not 0 <= nx <= N - 1 or not 0 <= ny <= N - 1:
        ans = True
        cnt += 1
        break

    if field[nx][ny] == '.':
        # if not 0 <= nx + dxy[d][0] <= N - 1 or not 0 <= ny + dxy[d][1] <= N - 1:
        #     ans = True
        #     cnt += 1
        #     break

        if d not in visited[nx][ny]:
            cnt += 1
            visited[nx][ny].append(d)
            tmp_d = (d + 1) % 4
            next_nx = nx + dxy[tmp_d][0]
            next_ny = ny + dxy[tmp_d][1]
            if field[next_nx][next_ny] == '#':
                pos.append([nx, ny])
            else:

                if d not in visited[next_nx][next_ny]:
                    cnt += 1
                    visited[next_nx][next_ny].append(tmp_d)
                    pos.append([next_nx, next_ny])
                    d = tmp_d
        else:
            break
    else:
        d -= 1
        if d == -1:
            d = 3
        if d not in visited[x][y]:
            pos.append([x, y])
            visited[x][y].append(d)

if ans:
    print(cnt)
else:
    print(-1)