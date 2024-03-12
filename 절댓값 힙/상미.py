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
        
        if rightChildIndex < len(heap) and (abs(heap[rightChildIndex]) < abs(heap[leftChildIndex]) or (abs(heap[rightChildIndex]) == abs(heap[leftChildIndex]) and heap[rightChildIndex] < heap[leftChildIndex])):
            minChildIndex = rightChildIndex
        
        if abs(heap[currentIndex]) > abs(heap[minChildIndex]) or (abs(heap[currentIndex]) == abs(heap[minChildIndex]) and heap[currentIndex] > heap[minChildIndex]):
            heap[currentIndex], heap[minChildIndex] = heap[minChildIndex], heap[currentIndex]
            currentIndex = minChildIndex
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
