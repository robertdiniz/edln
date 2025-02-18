class Grafo:

    def __init__(self):
        self.adj = []

    def adicionar_vertice(self, v):
        if v < len(self.adj):
            print("Vertíce já existe")
            return
        while len(self.adj) <= v:
            self.adj.append([])

    def adicionar_aresta(self, v1, v2):
        tamanho_adj = len(self.adj)
        if v1 < tamanho_adj and v2 < tamanho_adj:
            self.adj[v2].append(v1)
            self.adj[v1].append(v2)
    
    def display_adj_list(self):
        for i in range(len(self.adj)):
            print(f"{i}: ", end="")
            for j in self.adj[i]:
                print(j, end=" ")
            print()

grafo = Grafo()
grafo.adicionar_vertice(0)
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(2)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(2, 1)
print(grafo.adj)
grafo.display_adj_list()