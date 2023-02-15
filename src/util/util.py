import math

def flipArray(arry):
    for index in range(math.floor(len(arry) / 2)):
        temp = arry[index]
        arry[index] = arry[len(arry) - index - 1]
        arry[len(arry) - index - 1] = temp
    return arry

def inverseArray(arry):
    m = len(arry)
    n = len(arry[0])
    inversedArray = [[0] * m for _ in range(n)]
    for i in range (n):
        for j in range(m):
            inversedArray[i][j] = arry[j][i]
    return inversedArray



