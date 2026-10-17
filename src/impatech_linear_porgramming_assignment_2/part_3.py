from PIL import Image
from .part_2 import Graph, EncoderID, getGraph
from .part_1 import getScaledImage, getPreprocessedImage


def _getCoords(id: int, scale) -> tuple:
    i, j = EncoderID.decode(id)
    return (round(j * scale + scale/2), round(i * scale + scale/2))

def _drawLine(img: Image.Image, a: tuple, b: tuple, thick: int, color: tuple = (255, 0, 0), offplace: int = 0):
    """
        Draw a thick line between point A and point B
    """
    x1, y1 = a
    x2, y2 = b
    # assert(y1 == y2) # Points must have same Y

    swaped = y1 != y2
    if swaped: x1, x2, y1, y2 = y1, y2, x1, x2
    
    if x1 > x2: x2, x1 = x1, x2

    for _diff in range(x1 + offplace, x2+1 - offplace):
        for _thick in range(-thick, thick+1):
            if swaped:
                img.putpixel((y1 + _thick, _diff), color)
            else:
                img.putpixel((_diff, y1 + _thick), color)

def _drawCircle(img: Image.Image, center: tuple, radius: int, color:tuple = (255, 0, 0)):
    """
        Draw a circle with given center and radius
    """
    cx, cy = center
    for x in range(cx - radius, cx + radius + 1):
        for y in range(cy - radius, cy + radius + 1):
            if (x - cx)**2 + (y - cy)**2 <= radius**2:
                img.putpixel((x, y), color)

def drawGraph(scale: int = 40, show: bool = True, graph: Graph = None, lineOffPlace: int = 0, lineThick: int = 10, circleRadius: int = 10):
    if graph is None: graph = getGraph()

    dim = EncoderID.getDim()
    img: Image.Image = getScaledImage(scale)
    
    for a,b in graph.edges:
        x1, y1 = _getCoords(a, scale)
        x2, y2 = _getCoords(b, scale)

        _drawLine(img, (x1, y1), (x2, y2), lineThick, (255, 0, 0), offplace=lineOffPlace)
    
    for v in graph.adj_list.keys():
        x, y = _getCoords(v, scale)
        
        if v == graph.start or v == graph.end:
            _drawCircle(img, (x, y), circleRadius, (0, 255, 0))
        else:
            _drawCircle(img, (x, y), circleRadius, (0, 0, 255))
    if show: img.show()
    return img

if __name__ == "__main__":
    img_name = "labirinto.jpeg"
    _ = getGraph(getPreprocessedImage(img_name))
    drawGraph(scale=50, show=True, lineOffPlace=10, lineThick=2, circleRadius=10)