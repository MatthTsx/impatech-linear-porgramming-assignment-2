from .part_1 import getScaledImage
from .part_2 import Graph, EncoderID
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


def main():
    from .part_2 import getGraph
    from .part_1 import getPreprocessedImage
    from .part_5 import dijkstra
    from .part_6 import reconstruir_caminho

    graph = getGraph(getPreprocessedImage("labirinto.jpeg"))
    
    dists, parents = dijkstra(graph, graph.start)
    path = reconstruir_caminho(graph.start, graph.end, parents)

    DrawPath(path, scale=50, show=True, lineOffPlace=10, lineThick=2, circleRadius=10)


if __name__ == "__main__":
    main()
