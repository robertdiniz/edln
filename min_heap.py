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
            no_pai = (index - 1) // 2
            if self.heap[index] < self.heap[no_pai]:
                self.heap[index], self.heap[no_pai] = self.heap[no_pai], self.heap[index]
                index = no_pai
            else:
                break

    def remover_raiz(self):
        if len(self.heap) == 0:
            return None
        
        valor_raiz = self.heap[0] # 3
        self.heap[0] = self.heap.pop() # [0] = 6
        self.descer(0) # index
        self.display_heap()
        return valor_raiz
    
    def descer(self, index):
        tamanho = len(self.heap) # 4

        while True: # 6 4 15 10
            f_esquerda = 2 * index + 1 # 1
            f_direita = 2 * index + 2 # 2
            menor = index # 0

            if f_esquerda < tamanho and self.heap[f_esquerda] < self.heap[menor]: # 6 4 15 10
                print(f'[{f_esquerda}] = {self.heap[f_esquerda]} é menor que [{menor}] = {self.heap[menor]}')
                menor = f_esquerda
            
            if f_direita < tamanho and self.heap[f_direita] < self.heap[menor]:
                menor = f_direita
            
            if menor != index:
                print(f'{menor} - {index}')
                self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index] # 4 6 15 10
                index = menor
            else:
                print(f'{menor} - {index} agora é')
                break

    def display_heap(self):
        print(f'Heap atual: {self.heap}')


min_heap = MinHeap()

# dados que eu tava usando pra teste 👌
# min_heap.insert(10)
# min_heap.insert(4)
# min_heap.insert(15)
# min_heap.insert(6)
# min_heap.insert(3)

min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(1)
min_heap.insert(15)
min_heap.insert(30)
min_heap.insert(25)

print(min_heap.heap)

min_value = min_heap.remover_raiz()
print(min_value)