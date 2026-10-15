from PIL import Image
from .part_1_2 import getPreprocessedImage

_dims = None

class EncoderID:
    @staticmethod
    def set(dim: tuple):
        global _dims
        _dims = dim
    
    @staticmethod
    def encode(i: int, j: int) -> int:
        if _dims is None: raise ValueError("dims is not set. Please set with EnconderID.set(dim) before using this method.")
        return i*_dims[1] + j
    
    @staticmethod
    def decode(id: int) -> tuple:
        if _dims is None: raise ValueError("dims is not set. Please set with EnconderID.set(dim) before using this method.")
        return (id // _dims[1], id % _dims[1])

def checkOverflow(i: int, j: int) -> bool:
    if _dims is None: raise ValueError("dims is not set. Please set with EnconderID.set(dim) before using this method.")
    return not (0 <= i < _dims[0] and 0 <= j < _dims[1])



class Graph:
    def __init__(self, dim: tuple):
        """
            dim: (rows, cols) of the graph
            sz: maximum number of vertices in the graph
        """
        self.dim = dim
        self.sz = dim[0] * dim[1]
        
        self.edges = []
        self.adj_list: dict[int, list[int]] = {}

    def build(self, binary_matrix: list):
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if binary_matrix[i][j] == 0: continue
                _id = EncoderID.encode(i, j)

                for di, dj in [(1, 0), (0, 1)]:
                    ni, nj = i + di, j + dj

                    if not checkOverflow(ni, nj) and binary_matrix[ni][nj] == 1:
                        neighbor_id = EncoderID.encode(ni, nj)
                        self.adj_list.setdefault(_id, []).append(neighbor_id)
                        self.adj_list.setdefault(neighbor_id, []).append(_id)
                        self.edges.append((_id, neighbor_id))


if __name__ == "__main__":
    img_nome = "labirinto.jpeg"
    img_path = f"assets/{img_nome}"

    matriz_recebida = getPreprocessedImage(img_nome)
    img_original = Image.open(img_path).convert('L')

    EncoderID.set((len(matriz_recebida), len(matriz_recebida[0])))

    grafo = Graph(_dims)
    grafo.build(matriz_recebida)

    print(_dims)
    print(f"Número de vértices: {len(grafo.adj_list)} \nNúmero de arestas: {len(grafo.edges)}")
    # print(f"Conjunto de arestas: {grafo.edges}")
    # print(f"Lista de adjacência: {grafo.adj_list}")