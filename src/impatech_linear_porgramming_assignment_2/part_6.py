from .part_5 import dijkstra
from .part_2 import Graph, getGraph
from .part_1 import getPreprocessedImage


# English translation to my fellas: rebuild path
def reconstruir_caminho(s: int, t: int, parents: list[int]) -> list[int]:
    if t == s:
        return [s]
    else:
        return reconstruir_caminho(s, parents[t], parents) + [t]
    

if __name__ == "__main__":
    graph = getGraph(getPreprocessedImage("labirinto.jpeg"))
    dists, parents = dijkstra(graph, graph.start)

    path = reconstruir_caminho(graph.start, graph.end, parents)
    print(path)
    
    print("------------------------------")
    print("Cost of the path:", dists[graph.end])
    print("Number of moviments: ", len(path)-1)
    print("Number of vertices: ", len(path))
    print("Computation time of the path: dijkstra O(E log V), but initiation of parents is O(graph.sz) which in this case is 41*41 = 1681 which is bigger than E log V")