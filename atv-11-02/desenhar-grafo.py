import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def carregar_grafo_csv(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['origem'], row['destino'], weight=row['peso'])
    return G

def desenhar_grafo(G):
    pos = nx.spring_layout(G)
    pesos = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    
    plt.show()

grafo = carregar_grafo_csv("grafo.csv")
desenhar_grafo(grafo)
