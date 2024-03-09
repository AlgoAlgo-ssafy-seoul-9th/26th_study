# pypy에서만 통과, python3에서는 시간초과

def enq(d):
    global last
    last += 1       # 마지막 노드 추가
    H[last] = d
    c = last
    p = c//2
    while p>=1 and (abs(H[p])>abs(H[c]) or (abs(H[p])==abs(H[c]) and H[p]>H[c])): # 부모의 절대값이 자식의 절대값보다 크면
        H[p], H[c] = H[c], H[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = H[1]
    H[1] = H[last]  # 마지막 노드를 루트에 복사하고
    last -= 1       # 마지막 노드 삭제
    p = 1           # 루트부터
    c = 2          # 왼쪽자식
    while c<=last:     # 왼쪽 자식이 존재하면
        if c+1<=last and ((abs(H[c]) > abs(H[c+1])) or (abs(H[c])==abs(H[c+1]) and H[c]>H[c+1])): # 오른쪽 자식도 있고 절대값이 더 작으면
            c += 1         # 오른쪽 자식 선택
        if abs(H[p]) > abs(H[c]) or (abs(H[p])==abs(H[c]) and H[p]>H[c]):   # 절대값이 작거나, 절대값 같으면 더 작은 수가 있으면
            H[p], H[c] = H[c], H[p] # 교환
            p = c                   # 자식을 새로운 부모로
            c = p*2                 # 왼쪽 자식부터
        else:
            break
    return tmp

N = int(input())
H = [0] * (N+1)     # 최대 N개, 최소힙
last = 0
arr = [int(input()) for _ in range(N)]  # 시간초과 대비

ans = ''
#for _ in range(N):
for m in arr:
    #m = int(input())
    if m==0:
        if last == 0:
            ans += '0\n'
        else:
            ans += str(deq())+'\n'
    else:
        enq(m)
print(ans)
