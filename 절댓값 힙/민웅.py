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
