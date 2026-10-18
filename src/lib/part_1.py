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

def makeBinImage(path: str, image):
    with open(path, "w") as file:
        for i in range(len(image)):
            for j in range(len(image[0])):
                file.write(str(image[i][j]) + " ")
            file.write("\n")



def main():
    img_nome = "labirinto.jpeg"
    getPreprocessedImage(img_nome)
    makeBinImage("assets/labirinto_bin.txt", _bn)
    getScaledImage(40).show()


if __name__ == "__main__":
    main()
