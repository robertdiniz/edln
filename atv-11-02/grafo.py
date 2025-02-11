import networkx as nx

# G = nx.Graph()

class Grafo:

    def __init__(self):
        self.adj = []

    def adicionar_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj.append([])

    def adicionar_arestas(self, v1, v2):
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)


    def mostrar_grafo(self):
        for i in range(len(self.adj)):
            print(f"{i}: {self.adj[i]}")
    
            

grafo = Grafo()
grafo.adicionar_vertice(0)
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_arestas(0, 1)
grafo.adicionar_arestas(0, 2)
grafo.adicionar_arestas(2, 1)
print(grafo.adj)
grafo.mostrar_grafo()
# nx.draw(G)