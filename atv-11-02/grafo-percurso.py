class No:
    
    def __init__(self, value, weight):
        self.value = value
        self.next = None
        self.weight = weight
    
    
class List:

    def __init__(self):
        self.head = None


class Grafo:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = [List() for _ in range(self.num_vertices)]
        self.custo_maximo = None
        self.caminho_maximo = []
    
    def adicionar_vertice(self, v):
        if v >= self.num_vertices:
            self.adj.extend(List() for _ in range(v + 1 - self.num_vertices))
            self.num_vertices = v + 1
    
    def adicionar_aresta(self, v1, v2, peso):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            novo_no = No(v2, peso)
            novo_no.next = self.adj[v1].head
            self.adj[v1].head = novo_no

            novo_no = No(v1, peso)
            novo_no.next = self.adj[v2].head
            self.adj[v2].head = novo_no
        else:
            print("você tentou adicionar uma aresta com vértices que não existe.")
    
    def imprimir_grafo(self):
        for i in range(self.num_vertices):
            print(f"Vértice {i}: ", end="")
            current = self.adj[i].head
            while current:
                print(f"-> [{current.value} - {current.weight}] ", end="")
                current = current.next
            print()
    
    def bfs_menor_salto(self, origem, destino):
        if origem >= self.num_vertices or destino >= self.num_vertices:
            return "Cidade não encontrada."
        
        fila = [(origem, 0)]
        visitados = set()
        visitados.add(origem)

        while fila:
            no_atual, saltos = fila.pop(0)

            if no_atual == destino:
                return f"Menor número de paradas entre {origem} e {destino}: {saltos}"

            atual = self.adj[no_atual].head
            while atual:
                if atual.value not in visitados:
                    visitados.add(atual.value)
                    fila.append((atual.value, saltos + 1))
                atual = atual.next

        return "Nenhum caminho encontrado."
    
    def dfs_maior_custo(self, origem, destino):
        self.custo_maximo = None
        self.caminho_maximo = []
        visitados = set()
        self.dfs_recursivo(origem, destino, visitados, 0, [])
        return self.custo_maximo, self.caminho_maximo

    def dfs_recursivo(self, atual, destino, visitados, custo_atual, caminho_atual):
        visitados.add(atual)
        caminho_atual.append(atual)

        if atual == destino:
            if self.custo_maximo is None or custo_atual > self.custo_maximo:
                self.custo_maximo = custo_atual
                self.caminho_maximo = caminho_atual[:]
        else:
            vizinho = self.adj[atual].head
            while vizinho:
                if vizinho.value not in visitados:
                    self.dfs_recursivo(vizinho.value, destino, visitados, custo_atual + vizinho.weight, caminho_atual)
                vizinho = vizinho.next

        visitados.remove(atual)
        caminho_atual.pop()
    



grafo = Grafo(6)
grafo.adicionar_aresta(0, 1, 5)
grafo.adicionar_aresta(1, 2, 10)
grafo.adicionar_aresta(2, 3, 15)
grafo.adicionar_aresta(3, 4, 20)
grafo.adicionar_aresta(4, 5, 30)
grafo.adicionar_aresta(1, 5, 25)
grafo.imprimir_grafo()
print(grafo.bfs_menor_salto(0, 5))
custo, caminho = grafo.dfs_maior_custo(0, 5)
print(custo, caminho)