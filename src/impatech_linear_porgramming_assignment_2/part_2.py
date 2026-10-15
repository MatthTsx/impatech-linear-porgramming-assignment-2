from PIL import Image
from .part_1 import getPreprocessedImage

_dims = None
_graph = None

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
    
    def getDim() -> tuple:
        if _dims is None: raise ValueError("dims is not set. Please set with EnconderID.set(dim) before using this method.")
        return _dims

def checkOverflow(i: int, j: int) -> bool:
    if _dims is None: raise ValueError("dims is not set. Please set with EnconderID.set(dim) before using this method.")
    return not (0 <= i < _dims[0] and 0 <= j < _dims[1])


class Graph:
    def __init__(self, dim: tuple, _start: tuple = None, _end: tuple = None):
        """
            dim: (rows, cols) of the graph
            sz: maximum number of vertices in the graph
        """
        self.dim = dim
        self.sz = dim[0] * dim[1]
        
        if _start is not None and _end is not None:
            self.start = EncoderID.encode(_start[0], _start[1])
            self.end = EncoderID.encode(_end[0], _end[1])
        else:
            self.start = None
            self.end = None
        
        self.edges = []
        self.adj_list: dict[int, list[int]] = {}

    def _build(self, binary_matrix: list):
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


def getGraph(bn: list = None):
    global _graph
    
    if bn is not None:
        if _dims is None:
            EncoderID.set((len(bn), len(bn[0])))
        # We'll assume that the starting points and end points are aswell not initialized when this is called
        # Otherwise, we would make a global variable for that matter just like _dim
        start = None
        end = None

        
        # Check if theres points in the first and last row, otherwise check the first and last column
        for i in bn[0]:
            if i == 1:
                start = (0, bn[0].index(i))
                break
            
        for i in bn[-1]:
            if i == 1:
                end = (len(bn)-1, bn[-1].index(i))
                break
            
        if start is None:
            for i in range(len(bn)):
                if bn[i][0] == 1:
                    start = (i, 0)
                    break
        if end is None:
            for i in range(len(bn)):
                if bn[i][-1] == 1:
                    end = (i, len(bn[0])-1)
                    break

        _graph = Graph(_dims, start, end)
        _graph._build(bn)
    elif _graph is None:
        raise ValueError("Graph not initialized. Call getGraph(bn: binary matrix) first.")
    return _graph


if __name__ == "__main__":
    img_nome = "labirinto.jpeg"
    img_path = f"assets/{img_nome}"

    matriz_recebida = getPreprocessedImage(img_nome)
    img_original = Image.open(img_path).convert('L')

    EncoderID.set((len(matriz_recebida), len(matriz_recebida[0])))

    grafo = getGraph(matriz_recebida)

    print(_dims)
    print(f"Número de vértices: {len(grafo.adj_list)} \nNúmero de arestas: {len(grafo.edges)}")
    # print(f"Conjunto de arestas: {grafo.edges}")
    # print(f"Lista de adjacência: {grafo.adj_list}")