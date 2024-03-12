# python 은 dp 배열을 만들면 통과할 수 없다..
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