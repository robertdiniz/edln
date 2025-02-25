class No:
    
    def __init__(self, value):
        self.value = value
        self.next = None
    
class List:

    def __init__(self):
        self.head = None


class Grafo:

    def __init__(self, vertices):
        self.num_vertices = vertices
        self.adj = [List() for _ in range(self.num_vertices)]
    
    def adicionar_vertice(self, v):
        if v >= self.num_vertices:
            self.adj.extend(List() for _ in range(v + 1 - self.num_vertices))
            self.num_vertices = v + 1
    
    def adicionar_aresta(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            novo_no = No(v2)
            novo_no.next = self.adj[v1].head
            self.adj[v1].head = novo_no

            novo_no = No(v1)
            novo_no.next = self.adj[v2].head
            self.adj[v2].head = novo_no
        else:
            print("você tentou adicionar uma aresta com vértices que não existe.")
    
    def imprimir_grafo(self):
        for i in range(self.num_vertices):
            print(f"Vértice {i}: ", end="")
            current = self.adj[i].head
            while current:
                print(f"-> {current.value} ", end="")
                current = current.next
            print()


grafo = Grafo(5)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 4)
grafo.imprimir_grafo()
print(len(grafo.adj))

print()
grafo.adicionar_vertice(6) 
print(len(grafo.adj))

grafo.adicionar_aresta(2, 6)
grafo.adicionar_aresta(7, 8)
grafo.adicionar_aresta(0, 4)
grafo.imprimir_grafo()