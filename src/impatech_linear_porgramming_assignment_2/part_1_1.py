from PIL import Image

def _BinaryImage(img: Image) -> list:
    """
        returns the binary matrix such that each pixel is converted into binary
    """
    dims = img.size
    binaryMatrice = [[0 for _ in range(dims[0])] for _ in range(dims[1])]
    
    for i in range(dims[0]):
        for j in range(dims[1]):
            _x,_y,_z = img.getpixel((i,j))

            if (_x + _y + _z)/3.0 > 255.0/2.0:
                binaryMatrice[j][i] = 1
    return binaryMatrice


def _testBinaryImage():
    """
        Testing if _BinaryImage actually works with a more visable Image dimension like
    """
    
    img = Image.new("RGB", (10,10))
    img.putpixel((4,4), (255,255,255))
    
    print(_BinaryImage(img))


def _cropBinaryImage(binaryImage: list):
    """
        This function cuts the binary matrix so that their borders are 0 on their majority
    """
    
    coords = [0,0,0,0]
    dim = (len(binaryImage), len(binaryImage[0]))
    
    # Get vertical cuts
    for k in range (2):
        aux = []
        for i in range(dim[0]):
            x = 0 if k == 0 else dim[1]-1
            for j in range(dim[1]):
                nwx = j if k == 0 else dim[1]-1 - j
                if(binaryImage[i][nwx] == 0): break
                x = nwx
            aux.append(x)
        aux.sort()
        xmedian = aux[int(len(aux)/2)]
        coords[k] = xmedian
    
    # horizontal cuts
    for k in range(2):
        aux = []
        for j in range(dim[1]):
            y = 0 if k == 0 else dim[0]-1
            for i in range(dim[0]):
                nwy = i if k == 0 else dim[0]-1-i
                if(binaryImage[nwy][j] == 0): break
                y = nwy
            aux.append(y)
        aux.sort()
        ymedian = aux[int(len(aux)/2)]
        coords[2+k] = ymedian
    
    return [binaryImage[i][coords[0]+1: coords[1]] for i in range(coords[2]+1, coords[3])]


def getBinaryImage(path: str, crop: bool = True) -> list:
    """
        Get Binary Image
    """
    
    img = Image.open(f"assets/{path}")
    img.convert("L")
    
    if crop: return _cropBinaryImage(_BinaryImage(img))
    return _BinaryImage(img)

def _print_test(bn: list, show: bool = True):
    """
        Print the binary image matrix bn
    """
    dim = (len(bn), len(bn[0]))
    img = Image.new("RGB", (dim[1], dim[0]))
    
    for i in range(dim[0]):
        for j in range(dim[1]):
            x = bn[i][j]*255
            img.putpixel((j,i), (x,x,x))
    
    if show: img.show()
    return img

def getSizedImage(bimg: list, sizes: tuple):
    img = _print_test(bimg, False)
    
    return img.resize(sizes, resample=Image.Resampling.NEAREST)



if __name__ == "__main__":
    bn = getBinaryImage("labirinto.jpeg")
    _print_test(bn)
    getSizedImage(bn, (740,740)).show()
    pass