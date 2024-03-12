import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


N = int(input())
start = list(map(int, input().split()))
# 벽에 닿는 것을 감지하기 위해 사이드에 "." 추가
field = ["." * (N+2)]+["."+input().strip()+"." for _ in range(N)]+["." * (N+2)]
# 방향 설정
# 0: 오, 1: 위, 2 :왼, 3: 아래
direction = [(0,1), (-1, 0), (0, -1), (1,0)]
# 방문처리(최대 4번까지 방문가능 <4)
visited = [[0] * (N+2) for _ in range(N+2)]
visited[start[0]][start[1]] = 1

def dfs(i:int, j:int, cnt:int, dr:int):
    if i == 0 or i == N+1 or j == 0 or j == N+1:
        return cnt
    # 벽 인덱스 및 벽 위치
    wall = (dr+3)%4 
    walli, wallj = i+direction[wall][0], j+direction[wall][1]
    # 오른손에 벽이 있을 경우
    if field[walli][wallj] =="#":
        # 갈 수 있으면 감
        for d in range(dr, dr+4):
            di, dj = direction[d%4]
            ni, nj = i+di, j+dj
            if field[ni][nj] != "#":
                if visited[ni][nj]<4:
                    visited[ni][nj] += 1
                    return dfs(ni, nj, cnt+1, d%4)
                else:   # 4번째 방문하면 나갈 수 없음을 감지하고 포기
                    return -1
    else:   
    # 벽이 없으면 그 쪽으로 이동
        if visited[walli][wallj] < 4:
            visited[walli][wallj] += 1
            return dfs(walli, wallj, cnt+1, wall)
    
    return -1
    

print(dfs(start[0], start[1], 0, 0))