# pai = (index - 1 ) // 2
# filho esquerda = 2 * index + 1
# filho direita = 2 * index + 2

class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.subir(len(self.heap) - 1)
        self.display_heap()

    def subir(self, index):
        while index > 0:
            no_pai = (index - 1) // 2 
            if self.heap[index] > self.heap[no_pai]:
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

        while True:
            f_esquerda = 2 * index + 1 
            f_direita = 2 * index + 2 
            menor = index

            if f_esquerda < tamanho and self.heap[f_esquerda] > self.heap[menor]:
                menor = f_esquerda 
            
            if f_direita < tamanho and self.heap[f_direita] > self.heap[menor]:
                menor = f_direita
            
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

        if new_priority > old_priority:
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

    def constroi_heap(self, lista):
        # recebe uma lista e transforma em heap (no caso minheap)
        while len(lista) > 0:
            self.insert(lista.pop(0))


# max_heap = MaxHeap()

# max_heap.heap = [92, 85, 90, 47, 91, 34, 20, 40, 46]

# max_heap.change_priority(4, 93)

# min_heap.constroi_heap(lista_teste)

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