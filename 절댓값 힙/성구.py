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