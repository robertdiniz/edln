# pai = (index - 1 ) // 2
# filho esquerda = 2 * index + 1
# filho direita = 2 * index + 2

class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.subir(len(self.heap) - 1)
        self.display_heap()

    def subir(self, index):
        while index > 0:
            no_pai = (index - 1) // 2 # [3] = 4
            if self.heap[index] < self.heap[no_pai]:
                self.heap[index], self.heap[no_pai] = self.heap[no_pai], self.heap[index]
                self.display_heap()
                index = no_pai
            else:
                break

    def remover_raiz(self):
        if len(self.heap) == 0:
            return None
        
        valor_raiz = self.heap[0] 

        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop() 
            self.descer(0)
        else:
            self.heap.pop()

        self.display_heap()
        return valor_raiz
    
    def descer(self, index):
        tamanho = len(self.heap)

        while True: # index = 4
            f_esquerda = 2 * index + 1 
            f_direita = 2 * index + 2 
            menor = index # 1

            if f_esquerda < tamanho and self.heap[f_esquerda] < self.heap[menor]:
                menor = f_esquerda # [3] = 10
            
            if f_direita < tamanho and self.heap[f_direita] < self.heap[menor]:
                menor = f_direita # [4] = 15 < [3] = 10 
            
            if menor != index:
                self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index] 
                index = menor
                self.display_heap()
            else:
                break

    def change_priority(self, index, new_priority):
        old_priority = self.heap[index] # [8] = 9
        self.heap[index] = new_priority # 3

        self.display_heap()

        if new_priority < old_priority:
            self.subir(index)
        else:
            self.descer(index)


    def display_heap(self):
        print(f'Heap atual: {self.heap}')

    def get_high_priority(self):
        return self.heap[0]
    
    def heap_sort(self):

        sorted_heap = []

        while len(self.heap) > 0:
            sorted_heap.append(self.remover_raiz())

        return sorted_heap


# min_heap = MinHeap()

# dados que eu tava usando pra teste 👌
# min_heap.insert(10)
# min_heap.insert(4)
# min_heap.insert(15)
# min_heap.insert(6)
# min_heap.insert(3)

# min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(20)
# min_heap.insert(1)
# min_heap.insert(15)
# min_heap.insert(30)
# min_heap.insert(25)

# min_heap.change_priority(1, 50)
# min_heap.change_priority(1, 8)


# heap_ordenado = min_heap.heap_sort()
# print(heap_ordenado)

# min_heap.remover_raiz()
# min_heap.remover_raiz()
# min_heap.remover_raiz()

# min_value = min_heap.remover_raiz()
# print(min_value)