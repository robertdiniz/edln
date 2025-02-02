# index_pai = (index-1)//2
# filho_esquerda = (index*2)+1
# filho_direta = (index*2)+2

class MaxHeap():

    def __init__(self):
        self.heap = []
    
    # retorna o elemento com maior prioridade
    def get_max(self):
        return self.heap[0]
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(value, len(self.heap) - 1) # 6, 5
    
    def heapify_up(self, value, index):
        index_pai = (index - 1) // 2 # 2
        if index > 0 and self.heap[index] > self.heap[index_pai]: # 1 true,  2 true 
            self.heap[index], self.heap[index_pai] = self.heap[index_pai], self.heap[index]
            self.heapify_up(value, index_pai) # 6, 2
            self.print_maxheap()

    def remove_root(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]
        last_element = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.heapify_down(0)
        
        return root

    def heapify_down(self, index): # 0
        current = index # 0
        filho_esquerda = (index * 2) + 1 #  1
        filho_direita = (index * 2) + 2 # 2

        if filho_esquerda < len(self.heap) and self.heap[filho_esquerda] > self.heap[index]: # true, true
            current = filho_esquerda # 1
        
        if filho_direita < len(self.heap) and self.heap[filho_direita] > self.heap[index]:
            current = filho_direita
        
        if current != index: # 1, 0
            self.heap[index], self.heap[current] = self.heap[current], self.heap[index]
            current = index # 0
            self.heapify_down(current)
    
    def change_priority(self, index, new_value):
        old_priority = self.heap[index]
        self.heap[index] = new_value

        self.print_maxheap()

        if new_value > old_priority:
            self.heapify_up(new_value, index=index)
        else:
            self.heapify_down(index)

    def heap_sort(self, array):
        temp_heap = MaxHeap()

        for value in array:
            temp_heap.insert(value)
        
        sorted_list = []
        while len(temp_heap.heap) > 0:
            max_value = temp_heap.remove_root()
            sorted_list.append(max_value)
        
        return sorted_list[::-1]
            


    def print_maxheap(self):
        print(self.heap)

    

if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)
    max_heap.insert(30)
    max_heap.insert(40)

    max_heap.change_priority(2, 50)
    max_heap.change_priority(1, 5)
    max_heap.print_maxheap()

    print(max_heap.heap_sort([9, 4, 3, 8, 10, 2, 5] ))

    