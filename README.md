# 26th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [절댓값 힙](https://www.acmicpc.net/problem/11286)

### ❗ heapq 쓰지 않고 만들어 쓰기 ❗

### [민웅](./절댓값%20힙/민웅.py)

```py


```

### [상미](./절댓값%20힙/상미.py)

```py

```

### [성구](./절댓값%20힙/성구.py)

```py

```

### [승우](./절댓값%20힙/승우.py)

```py


```

### [영준](./절댓값%20힙/영준.py)

```py


```


<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [트리에 구슬 놓기](https://www.codetree.ai/problems/placing-marbles-on-the-tree/description)

### [민웅](./트리에%20구슬%20놓기/민웅.py)

```py

```

### [상미](./트리에%20구슬%20놓기/상미.py)

```py

```

### [성구](./트리에%20구슬%20놓기/성구.py)

```py
```

### [승우](./트리에%20구슬%20놓기/승우.py)

```py

```

### [영준](./트리에%20구슬%20놓기/영준.py)

```py

```

## [배낭에 보석 담기](https://www.codetree.ai/problems/put-gems-in-the-backpack/description)

### [민웅](./배낭에%20보석%20담기/민웅.py)

```py
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
```

### [상미](./배낭에%20보석%20담기/상미.py)

```py

```

### [성구](./배낭에%20보석%20담기/성구.py)

```py

```

### [승우](./배낭에%20보석%20담기/승우.py)

```py


```

### [영준](./배낭에%20보석%20담기/영준.py)

```py


```

## [미로 탈출하기](https://www.codetree.ai/problems/escape-the-maze/description)

### [민웅](./미로%20탈출하기/민웅.py)

```py
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
```

### [상미](./미로%20탈출하기/상미.py)

```py

```

### [성구](./미로%20탈출하기/성구.py)

```py

```

### [승우](./미로%20탈출하기/승우.py)

```py


```

### [영준](./미로%20탈출하기/영준.py)

```py


```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
