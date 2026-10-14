import matplotlib.image as mpimg
import numpy as np
from .part_1_2 import getPreprocessedImage

class Grafo:
    def __init__(self, tam):
        self.tam = tam
        self.lista = {i: [] for i in range(tam**2)} # Lista de adjacência do grafo
        self.arestas = [] # Arestas na forma (id_no(u), id_no(v))
        self.coords = [None] * (tam ** 2)

    def id_no(self, i, j):
        return(i * self.tam + j)

    def add_aresta(self, id_1, id_2):
        self.lista[id_1].append(id_2)
        self.lista[id_2].append(id_1)
        self.arestas.append((id_1, id_2))

    def construir(self, matriz):
        for i in range(self.tam):
            for j in range(self.tam):
                k = self.id_no(i, j)

                # Posições na matriz e na imagem 41x41 original
                lin = 2 * i + 1
                col = 2 * j + 1
                self.coords[k] = coords_originais(lin, col)

                # Varredura para baixo e direita
                if j < self.tam - 1: # Verificação horizontal
                    if matriz[lin][col + 1] == 1:
                        viz_id = self.id_no(i, j + 1)
                        self.add_aresta(k, viz_id)
                
                if i < self.tam - 1: # Verificação vertical
                    if matriz[lin + 1][col] == 1:
                        viz_id = self.id_no(i + 1, j)
                        self.add_aresta(k, viz_id)

tam = 20

img_nome = "labirinto.jpeg"
img_path = f"assets/{img_nome}"
matriz_recebida = getPreprocessedImage(img_nome)
img_original = mpimg.imread(img_path)

if img_original.ndim == 3:
    img_gray = img_original.mean(axis=2)
else:
    img_gray = img_original

pixels_pretos = np.where(img_gray < 0.5)
topo, base = pixels_pretos[0].min(), pixels_pretos[0].max()
esq, direita = pixels_pretos[1].min(), pixels_pretos[1].max()

lins = len(matriz_recebida)
cols = len(matriz_recebida[0])
escala_y = (base - topo) / lins
escala_x = (direita - esq) / cols

def coords_originais(lin, col):
    y = topo + (lin * escala_y) + (escala_y / 2)
    x = esq + (col * escala_x) + (escala_x / 2)
    return x, y

grafo = Grafo(tam)
grafo.construir(matriz_recebida)

print(f"Número de vértices: {len(grafo.lista)} \nNúmero de arestas: {len(grafo.arestas)}")
# print(f"Conjunto de arestas: {grafo.arestas}")
# print(f"Lista de adjacência: {grafo.lista}")