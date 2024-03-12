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
# 11286_절대값 힙_Absolute heap
import sys
input = sys.stdin.readline


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, num):
        self.heap.append((abs(num), num))
        self._up_move(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()[1]

        root_value = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self._down_move(0)
        return root_value

    def _up_move(self, idx):
        while idx > 0:
            if self.heap[idx] < self.heap[(idx-1) // 2]:
                self.heap[idx], self.heap[(idx-1) // 2] = self.heap[(idx-1) // 2], self.heap[idx]
                idx = (idx-1)//2
            else:
                break

    def _down_move(self, idx):
        length = len(self.heap)
        while True:
            l = 2*idx+1
            r = 2*idx+2
            min_value = idx

            # 왼쪽 자식 노드, 오른쪽 자식노드 순서로 검사
            if l < length and self.heap[l] < self.heap[min_value]:
                min_value = l

            if r < length and self.heap[r] < self.heap[min_value]:
                min_value = r

            # 바뀐적이 있으면 바꾸고 다시 진행
            if min_value != idx:
                self.heap[idx], self.heap[min_value] = self.heap[min_value], self.heap[idx]
                idx = min_value
            else:
                break


N = int(input())
hq = MinHeap()

for _ in range(N):
    tmp = int(input())
    if tmp != 0:
        hq.push(tmp)
    else:
        print(hq.pop())

```

### [상미](./절댓값%20힙/상미.py)

```py

```

### [성구](./절댓값%20힙/성구.py)

```py
# 11286 절댓값 힙
import sys
input = sys.stdin.readline


class AbsoluteHeap:

    def __init__(self, N:int) -> None:
        # 전체 길이를 미리 선정하여 heap list를 생성
        # 길이를 미리 저장
        self.tree = [0] * (2*N+2)
        self.length = 0

    # 힙 소트(시작 노드를 입력받음)
    # 시작 노드 0 -> root에서 아래로 내려감
    # 시작 노드 0이 아닌 다른 인덱스 -> 인덱스에서 위로 올라감
    def heap_sort(self, node:int) -> None:
        # 시작노드가 root 노드 일 때 -> 아래로 내려감
        if node == 0:
            
            while node < self.length:
                left, right = 2*node+1, 2*node+2
                # 길이를 넘어가면 트리에서 벗어남(leaf 노드가 0임)
                if node >= self.length:
                    break
                if left >= self.length and right >= self.length:
                    node += 1
                # leaf 노드에서 하나만 넘어가는 경우(leaf 노드가 없는 경우)    
                elif left >= self.length:   # 왼쪽 leaf 노드 0
                    # 절댓값이 작은 것 기준, 같을 땐 값이 작은 친구를 root 노드와 교환
                    if abs(self.tree[right]) < abs(self.tree[node]):
                        self.tree[right], self.tree[node] = self.tree[node], self.tree[right]
                    elif abs(self.tree[right]) == abs(self.tree[node]):
                        if self.tree[right] < self.tree[node]:
                            self.tree[right], self.tree[node] = self.tree[node], self.tree[right]
                    node = right    # 다음 탐색 확인
                    
                elif right >= self.length:  # 오른쪽 leaf 노드 0
                    if abs(self.tree[left]) < abs(self.tree[node]):
                        self.tree[left], self.tree[node] = self.tree[node], self.tree[left]
                    elif abs(self.tree[left]) == abs(self.tree[node]):
                        if self.tree[left] < self.tree[node]:
                            self.tree[left], self.tree[node] = self.tree[node], self.tree[left]
                    node = left
                else:
                    # 모두 범위 내의 경우(leaf 노드가 둘 다 있는 경우)
                    # 왼쪽 leaf 노드와 오른쪽 leaf 노드를 비교
                    # 더 작은 쪽 leaf 노드와 root 노드 비교 -> root 노드가 더 크다면 교환
                    
                    if abs(self.tree[left]) > abs(self.tree[right]):
                        if abs(self.tree[node]) > abs(self.tree[right]) or (abs(self.tree[node]) ==  abs(self.tree[right]) and self.tree[node] > self.tree[right]):
                            self.tree[node], self.tree[right] = self.tree[right], self.tree[node]
                            node = right
                    elif abs(self.tree[left]) == abs(self.tree[right]):
                        if self.tree[left] > self.tree[right]:
                            if abs(self.tree[node]) > abs(self.tree[right]) or (abs(self.tree[node]) ==  abs(self.tree[right]) and self.tree[node] > self.tree[right]):
                                self.tree[node], self.tree[right] = self.tree[right], self.tree[node]
                                node = right
                        else:
                            if abs(self.tree[node]) > abs(self.tree[left]) or (abs(self.tree[node]) ==  abs(self.tree[left]) and self.tree[node] > self.tree[left]):
                                self.tree[node], self.tree[left] = self.tree[left], self.tree[node]
                                node = left

                    else:
                        if abs(self.tree[node]) > abs(self.tree[left]) or (abs(self.tree[node]) ==  abs(self.tree[left]) and self.tree[node] > self.tree[left]):
                            self.tree[node], self.tree[left] = self.tree[left], self.tree[node]
                            node = left
                # 다음 노드를 탐색하지 더 이상 않아도 되는 경우 break
                if node != left and node != right:
                    break
                
        else:   # 시작 노드가 0이 아닌 경우 -> leaf 노드에서 root노드 쪽으로 탐색
            while node > 0:
                # 인덱스가 leaf 노드 기준 왼쪽(홀수), 오른쪽(짝수)
                # root node(N) -> left leaf node (2*N+1) / right leaf node (2*N + 2)
                if node % 2:    # left leaf node (2*N+1) -> (2*N+1)//2 = N
                    root = node // 2    
                else:           # right leaf node (2*N+2) -> (2*N+2) //2 -1 = N
                    root = node // 2 - 1
                
                # root 노드와 비교하여 교환할 여지가 있으면 교환하여 탐색 
                if abs(self.tree[root]) > abs(self.tree[node]) or (abs(self.tree[root]) == abs(self.tree[node]) and self.tree[root] > self.tree[node]):
                    self.tree[root], self.tree[node] = self.tree[node], self.tree[root]
                    node = root
                else:   # 교환할 필요 없으면 더 이상 탐색 X
                    break
                    
        return
        
    # 힙 푸시
    def push_num(self, num:int) -> None:
        # 마지막 노드에 추가하여 힙 소트(leaf -> root)
        self.tree[self.length] = num
        self.heap_sort(self.length)
        self.length += 1
        return
        
    # 힙 팝
    def pop_num(self) -> int:
        # root 노드를 제거한 후, 마지막 leaf 노드를 root 노드에 넣어 힙 소트(root -> leaf)
        if self.length == 0:
            return 0
        root = self.tree[0]
        self.tree[0], self.tree[self.length-1] = self.tree[self.length-1], 0
        self.length -= 1
        self.heap_sort(0)
        return root


def solution():
    N = int(input())
    # class 를 이용하여 절댓값 힙 구성
    AH = AbsoluteHeap(N)
    for _ in range(N):
        x = int(input())
        if x == 0:
            print(AH.pop_num())
        else:
            AH.push_num(x)
    return


if __name__ == "__main__":
    solution()
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
# python 은 dp 배열을 만들면 통과할 수 없다..
# 해설 보고 풀었습니다
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
# 트리 배열
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 트리 순회(후위)
def postorder(leaf, root):
    no_marble, marble = 0, 1
    for node in tree[leaf]:
        if node != root:    # 내려온 가지가 아니면
            nm, m = postorder(node, leaf)
            # leaf에서 가져온 값을 더해줌
            no_marble += m  # 구슬을 놓지 않을 땐, leaf에서 반드시 구슬을 놔야함
            marble += min(nm, m)    # 구슬을 놓을 땐 상관없음(최솟값 더하기 -> 저장)
    return no_marble, marble

print(min(postorder(1,0)))
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

[알고리즘 설명](https://l1m3kun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90%EC%99%80-%ED%9E%99Priority-Queue-Heap)

</details>
