# pai = (index - 1 ) // 2
# filho esquerda = 2 * index + 1
# filho direita = 2 * index + 2

class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.subir(len(self.heap) - 1) 

    def subir(self, index):
        while index > 0:
            no_pai = (index - 1) // 2
            print(self.heap)
            if self.heap[index] < self.heap[no_pai]:
                self.heap[index], self.heap[no_pai] = self.heap[no_pai], self.heap[index]
                index = no_pai
                print(self.heap)
            else:
                break

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(4)
min_heap.insert(15)
min_heap.insert(6)
min_heap.insert(3)

print(min_heap.heap)