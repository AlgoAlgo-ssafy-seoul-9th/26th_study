import sys
input = sys.stdin.readline

def push(heap, x):
    heap.append(x)
    currentIndex = len(heap) - 1
    while currentIndex > 0:
        parentIndex = (currentIndex - 1) // 2
        if abs(heap[currentIndex]) < abs(heap[parentIndex]) or (abs(heap[currentIndex]) == abs(heap[parentIndex]) and heap[currentIndex] < heap[parentIndex]):
            heap[currentIndex], heap[parentIndex] = heap[parentIndex], heap[currentIndex]
            currentIndex = parentIndex
        else:
            break

def pop(heap):
    if not heap:
        return 0
    
    minValue = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    
    currentIndex = 0

    while currentIndex * 2 + 1 < len(heap):
        leftChildIndex = currentIndex * 2 + 1
        rightChildIndex = currentIndex * 2 + 2
        minChildIndex = leftChildIndex

        # 오른쪽 자식 노드가 최소인 경우
        # 전체 노드 안 범위에서 왼쪽 자식 노드의 절댓값이 더 크거나 둘이 절댓값은 같지만 왼쪽 자식노드의 값이 더 클 때    
        if rightChildIndex < len(heap) and (abs(heap[rightChildIndex]) < abs(heap[leftChildIndex]) or (abs(heap[rightChildIndex]) == abs(heap[leftChildIndex]) and heap[rightChildIndex] < heap[leftChildIndex])):
            minChildIndex = rightChildIndex
        
        # 지금 노드의 절댓값이 최소 노드의 절댓값보다 크거나 절댓값은 같지만 지금 노드의 값이 더 클 때
        # 현재 노드의 값과 최소 노드의 값(왼쪽 자식 노드) 교환 후 현재 노드를 최소 노드로 갱신
        if abs(heap[currentIndex]) > abs(heap[minChildIndex]) or (abs(heap[currentIndex]) == abs(heap[minChildIndex]) and heap[currentIndex] > heap[minChildIndex]):
            heap[currentIndex], heap[minChildIndex] = heap[minChildIndex], heap[currentIndex]
            currentIndex = minChildIndex
        
        # 더 이상 바꿀 것이 없으면
        else:
            break

    return minValue

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        print(pop(heap))
    else:
        push(heap, x)
