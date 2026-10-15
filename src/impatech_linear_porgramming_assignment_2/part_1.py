from .part_1_2 import getPreprocessedImage as _getPreprocessedImage
from .part_1_1 import getScaledImage as _getScaledImage

_bn = None
def getPreprocessedImage(img_name: str = None):
    global _bn
    if img_name is not None:
        _bn = _getPreprocessedImage(img_name)
    elif _bn is None:
        raise ValueError("Binary Matrix not loaded. Please call getPreprocessedImage(img_name) first.")
    return _bn


def getScaledImage(multipliyer: int):
    if _bn is None:
        raise ValueError("Binary Matrix not loaded. Please call getPreprocessedImage(img_name) first.")
    return _getScaledImage(_bn, multipliyer)

if __name__ == "__main__":
    img_nome = "labirinto.jpeg"
    _bn = getPreprocessedImage(img_nome)
    getScaledImage(40).show()