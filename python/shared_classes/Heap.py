class HeapMax:
    def __init__(self):
        self.heap = []

    def heapify(self, heap):
        self.heap = heap.copy

        last_parent_node = len(self.heap) // 2 - 1

        while last_parent_node >= 0:
            
            last_parent_node -= 1

    def sift_down(self, index = 0):
        n = len(self.heap)

        while True:
            largest = index
            left_child = 2 * (index + 1)
            right_child = 2 * (index + 2)
            
            if left_child < n and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            if right_child < n and self.heap[right_child] > self.heap[largest]:
                largest = right_child
            if largest == index:
                break

            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            index = largest

    def heappush(self, val):
        return 

    def heappop(self):
        return 

    def heapmax(self):
        return 

list1 = [3, 2, 5, 6, 2, 4, 3, 5, 1]
heap1 = HeapMax()
heap1.heapify(list1)