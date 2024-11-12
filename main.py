import os
import time
from min_heap import MinHeap

# pai = (index - 1 ) // 2
# filho esquerda = 2 * index + 1
# filho direita = 2 * index + 2

def clear_console():
    # Limpa o console conforme o sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para esperar o usuário pressionar "Enter"
def wait_for_next():
    input("\nPressione 'Enter' para continuar para a próxima atividade...")
    clear_console()


if __name__ == "__main__":
    atv1 = MinHeap()
    # inserindo os dados da q1
    print('Q1 - Construindo o HEAP:')
    atv1.insert(10)
    atv1.insert(5)
    atv1.insert(20)
    atv1.insert(1)
    atv1.insert(15)
    atv1.insert(30)
    atv1.insert(25)

    # alterando prioridades
    print('Alterando Prioridades')
    atv1.change_priority(3, 50)
    atv1.change_priority(1, 8)

    # removendo os roots
    atv1.remover_raiz()
    atv1.remover_raiz()
    atv1.remover_raiz()

    # selecionando alta prioridade
    print(f'Elemento de alta prioridade: {atv1.get_high_priority()}')

    # mostrando heap ordenado
    print('Mostrando o heap ordenado')
    heap_atv1_sort = atv1.heap_sort()
    print(heap_atv1_sort)

    wait_for_next()

    # q2 - ordem crescente
    print('Q2 - Ordem Crescente')
    atv2 = MinHeap()
    atv2.insert(1)
    atv2.insert(2)
    atv2.insert(3)
    atv2.insert(4)
    atv2.insert(5)
    atv2.insert(6)
    atv2.insert(7)
    atv2.insert(8)
    atv2.insert(9)
    atv2.insert(10)

    # alterando prioridades
    print('Q2 - Alterando prioridades')
    atv2.change_priority(4, 15)
    atv2.change_priority(8, 3)

    # selecionando alta prioridade
    print(f'Elemento de alta prioridade: {atv2.get_high_priority()}')

    # removendo
    print('Removendo roots:')
    atv2.remover_raiz()
    atv2.remover_raiz()
    atv2.remover_raiz()
    atv2.remover_raiz()
    atv2.remover_raiz()

    # heap sort
    print('Heap Sort:')
    heap_atv2_sort = atv2.heap_sort()
    print(heap_atv2_sort)

    wait_for_next()

    # Q3 - Sequência Decrescente
    atv3 = MinHeap()

    print('Q3 - Inserindo dados no heap')
    atv3.insert(50)
    atv3.insert(40)
    atv3.insert(30)
    atv3.insert(20)
    atv3.insert(10)
    atv3.insert(5)
    atv3.insert(3)

    print('Alterando prioridades')
    atv3.change_priority(2, 60)
    atv3.change_priority(5, 1)

    # selecionando alta prioridade
    print(f'Elemento de alta prioridade: {atv3.get_high_priority()}')

    print('Removendo roots')
    atv3.remover_raiz()
    atv3.remover_raiz()
    atv3.remover_raiz()

    print('Heap Sort:')
    atv3_heap_sort = atv3.heap_sort()
    print(atv3_heap_sort)

    wait_for_next()

    # Q4 - Dados Aleatórios Maiores
    atv4 = MinHeap()

    atv4.insert(13)
    atv4.insert(26)
    atv4.insert(19)
    atv4.insert(17)
    atv4.insert(24)
    atv4.insert(31)
    atv4.insert(22)
    atv4.insert(11)
    atv4.insert(8)
    atv4.insert(20)
    atv4.insert(5)
    atv4.insert(27)
    atv4.insert(18)

    print('Alterando prioridades')
    atv4.change_priority(7, 35)
    atv4.change_priority(10, 12)

    # selecionando alta prioridade
    print(f'Elemento de alta prioridade: {atv4.get_high_priority()}')

    print('Removendo roots')
    atv4.remover_raiz()
    atv4.remover_raiz()
    atv4.remover_raiz()
    atv4.remover_raiz()

    print('Heap Sort:')
    atv4_heap_sort = atv4.heap_sort()
    print(atv4_heap_sort)
