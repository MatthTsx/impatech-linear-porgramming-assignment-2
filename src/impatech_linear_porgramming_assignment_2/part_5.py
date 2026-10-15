from .part_2 import Graph, getGraph
from .part_1 import getPreprocessedImage
import heapq


def dijkstra(graph: Graph, start: int, weight: int = 1):
    priority_queue = []
    qntVertices = graph.sz
    visited = [False] * (qntVertices + 3) # + 3 to prevent off by one errors
    parents = [None] * (qntVertices + 3)
    dists = [float('inf')] * (qntVertices + 3)

    for v in graph.adj_list[start]:
        priority_queue.append((weight, v, start))
    
    while len(priority_queue) > 0:
        c_weight, c_node, c_parent = heapq.heappop(priority_queue)
        if visited[c_node]: continue
        visited[c_node] = True
        
        parents[c_node] = c_parent
        dists[c_node] = c_weight
        
        for v in graph.adj_list[c_node]:
            if not visited[v]:
                heapq.heappush(priority_queue, (c_weight + weight, v, c_node))
    
    return dists, parents




if __name__ == "__main__":
    graph = getGraph(getPreprocessedImage("labirinto.jpeg"))
    dists, parents = dijkstra(graph, graph.start)
    print(dists)
    print(parents)