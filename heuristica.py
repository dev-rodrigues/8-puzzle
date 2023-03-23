def heuristica(filho, goal):
    distancia = 0
    for i in range(len(filho)):
        for j in range(len(filho[i])):
            if filho[i][j] != goal[i][j] and filho[i][j] != 0:
                (x, y) = posicao(goal, filho[i][j])
                d = abs(x - i) + abs(y - j)
                distancia += d
    return distancia


def posicao(matriz, elemento):
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor == elemento:
                return i, j
    else:
        return None
