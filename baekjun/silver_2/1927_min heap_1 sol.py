import sys
input = sys.stdin.readline

class minHeap:
    def __init__(self):
        self.heap = [0]

    def add(self, item):
        self.heap.append(item)
        if len(self.heap)>1:
            child_index = len(self.heap)-1
            parent_index = child_index//2
            self.up_swap(child_index, parent_index)
        
    def delete(self):
        if len(self.heap)-1:
            print(self.heap[1])
            del self.heap[1]
            if len(self.heap)-1:
                self.heap.insert(1, self.heap[len(self.heap)-1])
                del self.heap[len(self.heap)-1]
                parent_index = 1
                child_index = parent_index*2
                if child_index<=len(self.heap)-1:
                    self.down_swap(child_index, parent_index)
        else: print(0)


    def down_swap(self, child_index, parent_index):
        if child_index+1<=len(self.heap)-1:
            child_index = child_index+1 if self.heap[child_index]>self.heap[child_index+1] else child_index
        if self.heap[parent_index] <= self.heap[child_index]: return 0
        else:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            parent_index = child_index
            child_index = parent_index*2
            if child_index<=len(self.heap)-1:
                self.down_swap(child_index, parent_index)

    def up_swap(self, child_index, parent_index):
        if self.heap[parent_index] <= self.heap[child_index]: return 0
        else:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            child_index = parent_index
            parent_index = child_index//2
            self.up_swap(child_index, parent_index)    

heap = minHeap()
N = int(input())
for _ in range(N):
    if (q:=int(input())): heap.add(q)
    else:
        heap.delete()

