from .part_1_1 import getBinaryImage, _print_test


def _getMedian(bn: list):
    dim = (len(bn), len(bn[0]))
    
    aux = []
    visited = [[False for _ in range(dim[1])] for _ in range(dim[0])]
    for i in range(dim[0]):
        for j in range(dim[1]):
            if visited[i][j]: continue
            lstk = 1
            target = bn[i][j]
            
            for k in range(1, min(dim[0], dim[1])):
                if i+k >= dim[0] or j+k >= dim[1]: break
                
                doable = bn[i+k][j+k] == target and not visited[i+k][j+k]
                for ik in range(0, k):
                    doable &= bn[i+k][j+ik] == target and not visited[i+k][j+ik]
                    doable &= bn[i+ik][j+k] == target and not visited[i+ik][j+k]
                
                if not doable: break
                lstk = k+1
            
            for k in range(0, lstk):
                for ik in range(0, lstk):
                    visited[i+k][j+ik] = True
            aux.extend([lstk] * (lstk * lstk))

    aux.sort()
    return aux[int(len(aux)/2)]

def _getCellCount(lines: list, m: int):
    """
        Number of cells along each line. The real cell size is typicaly not an integer,
        so it is refined from m using the runs of equal pixels (a run of length l spans round(l/m) cells)
    """
    length = 0
    cells = 0
    for line in lines:
        run = 1
        for k in range(1, len(line)+1):
            if k < len(line) and line[k] == line[k-1]:
                run += 1
                continue
            if round(run/m) > 0:
                length += run
                cells += round(run/m)
            run = 1

    if cells == 0: return max(1, round(len(lines[0])/m))
    return max(1, round(len(lines[0]) * cells / length))

def _compress(bn: list, m: int):
    dim = (len(bn), len(bn[0]))

    # cells per axis, with the pixel boundaries spread evenly so the grid doesn't drift
    n = (_getCellCount([list(col) for col in zip(*bn)], m), _getCellCount(bn, m))
    ys = [round(k * dim[0] / n[0]) for k in range(n[0]+1)]
    xs = [round(k * dim[1] / n[1]) for k in range(n[1]+1)]

    compressed = []

    for ci in range(n[0]):
        compressed.append([])
        for cj in range(n[1]):
            ones = 0
            zero = 0

            for i in range(ys[ci], ys[ci+1]):
                for j in range(xs[cj], xs[cj+1]):
                    if bn[i][j] == 0: zero += 1
                    else: ones += 1

            if ones > zero: compressed[ci].append(1)
            else: compressed[ci].append(0)

    return compressed

def getPreprocessedImage(path: str):
    bimg = getBinaryImage(path)
    
    return _compress(bimg, _getMedian(bimg))

if __name__ == "__main__":
    cmp = getPreprocessedImage("labirinto.jpeg")
    _print_test(cmp)