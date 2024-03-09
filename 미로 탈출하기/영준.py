def f(i, j, N):
    T = 0
    dir = 0
    while 1<=i<=N and 1<=j<=N:
        if (visited[i][j]&(1<<dir)):
            return -1
        visited[i][j] |= 1<<dir
        ni1, nj1 = i + di[dir], j + dj[dir]   # 진행 방향
        ni2, nj2 = i + di[(dir+1)%8], j+dj[(dir+1)%8] #오른쪽 앞
        if maze[ni1][nj1] == '0':   # 진행방향 탈출
            return T+1
        elif maze[ni1][nj1]=='.' and maze[ni2][nj2]=='#':  # 직진
            i, j = ni1, nj1
            T += 1
        elif maze[ni1][nj1]=='.' and maze[ni2][nj2]=='.':  # 우회전
            visited[ni1][nj1] |= 1<<dir
            i, j = ni2, nj2
            T += 2
            dir = (dir+2)%8
        elif maze[ni1][nj1] == '#':  # 진행방향 벽
            dir = (dir+8-2)%8       # 반시계방향
        
    return T + 1


di = [0, 1, 1, 1, 0,-1,-1,-1]
dj = [1, 1, 0,-1,-1,-1, 0, 1]



N = int(input())
x, y = map(int, input().split())
maze = ['0'*(N+2)] + ['0'+input()+'0' for _ in range(N)] + ['0'*(N+2)]
visited = [[0] * (N+2) for _ in range(N+2)]

ans = f(x, y, N)
print(ans)
