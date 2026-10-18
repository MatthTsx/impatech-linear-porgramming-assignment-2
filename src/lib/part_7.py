from .part_1 import getScaledImage
from .part_2 import Graph, EncoderID, getGraph
from .part_3 import _drawLine, _drawCircle, _getCoords
from PIL import Image

def DrawPath(path: list[int], scale: int = 40, show: bool = True, graph: Graph = None, lineOffPlace: int = 0, lineThick: int = 10, circleRadius: int = 10):
    img: Image.Image = getScaledImage(scale)
    
    for i in range(1, len(path)):
        _drawLine(img, _getCoords(path[i-1], scale), _getCoords(path[i], scale), lineThick, (255, 0, 0), offplace=lineOffPlace)
        
    for i in path:
        if i == path[0]:
            _drawCircle(img, _getCoords(i, scale), circleRadius, (0, 255, 0))
        elif i == path[-1]:
            _drawCircle(img, _getCoords(i, scale), circleRadius, (0, 0, 255))
        else:
            _drawCircle(img, _getCoords(i, scale), circleRadius, (255, 0, 0))
    
    if show: img.show()
    return img

def DrawComb(path: list[int], scale: int = 40, show: bool = True, graph: Graph = None, lineOffPlace: int = 0, lineThick: int = 2, circleRadius: int = 10):
    if graph is None: graph = getGraph()
    img: Image.Image = getScaledImage(scale)

    for a,b in graph.edges:
            x1, y1 = _getCoords(a, scale)
            x2, y2 = _getCoords(b, scale)
    
            _drawLine(img, (x1, y1), (x2, y2), lineThick, (255, 127, 0), offplace=lineOffPlace)

    for v in graph.adj_list.keys():
            x, y = _getCoords(v, scale)
            _drawCircle(img, (x, y), circleRadius, (255, 127, 0))

    for i in range(1, len(path)):
            _drawLine(img, _getCoords(path[i-1], scale), _getCoords(path[i], scale), lineThick, (255, 0, 0), offplace=lineOffPlace)

    for i in path:
        _drawCircle(img, _getCoords(i, scale), circleRadius + 2, (255, 0, 0))

    _drawCircle(img, _getCoords(graph.start, scale), circleRadius + 5, (0, 255, 0))
    _drawCircle(img, _getCoords(graph.end, scale), circleRadius + 5, (0, 0, 255))
    
    if show: img.show()
    return img

def main():
    from .part_2 import getGraph
    from .part_1 import getPreprocessedImage
    from .part_5 import dijkstra
    from .part_6 import reconstruir_caminho

    graph = getGraph(getPreprocessedImage("labirinto.jpeg"))
    
    dists, parents = dijkstra(graph, graph.start)
    path = reconstruir_caminho(graph.start, graph.end, parents)

    DrawPath(path, scale=50, show=True, lineOffPlace=10, lineThick=2, circleRadius=10)

    DrawComb(path, scale=50, show=True, lineOffPlace=10, lineThick=2, circleRadius=10)


if __name__ == "__main__":
    main()
