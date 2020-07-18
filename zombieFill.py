NEIGHBORS = [[0,1], [0,-1], [-1, 0], [1, 0]]

def isInBounds(rows, cols, pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= rows or pos[1] >= cols:
        return False
    else:
        return True

def vecAdd(x, y):
    return [x[0] + y[0], x[1]+y[1]]

def getHumanNeighbors(z, matrix, r, c):
    zNeighbors = list()
    for N in NEIGHBORS:
      n = vecAdd(z, N)
      if isInBounds(r, c, n) and matrix[n[0]][n[1]] == 0:
          matrix[n[0]][n[1]] = 1
          zNeighbors.append(n)
    return zNeighbors
          

def humanDays(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """           
    
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    if cols == 0:
        return 0
    currentGen = list()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # Is a zombie
                currentGen.append([i,j])
    day = -1
    while len(currentGen) > 0:
        nextGen = list()
        for zombie in currentGen:
            nHumans = getHumanNeighbors(zombie, matrix, rows, cols)
            nextGen.extend(nHumans)
        currentGen = nextGen
        day += 1
    return day
