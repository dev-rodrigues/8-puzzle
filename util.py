import copy


def valida(x, y):
    r = True
    if x < 0 or x > 2:
        r = False
    if y < 0 or y > 2:
        r = False

    return r


def filhos(s):
    retorno = []
    x = None
    y = None

    # localizando 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                x = i
                y = j
    # sobe
    vx = x - 1
    vy = y
    if valida(vx, vy):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        retorno.append(cover)
    # desce
    vx = x + 1
    vy = y
    if valida(vx, vy):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        retorno.append(cover)
    # esquerda
    vx = x
    vy = y - 1
    if valida(vx, vy):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        retorno.append(cover)
        # direita
    vx = x
    vy = y + 1
    if valida(vx, vy):
        cover = copy.deepcopy(s)
        t = cover[vx][vy]
        cover[vx][vy] = cover[x][y]
        cover[x][y] = t
        retorno.append(cover)

    return retorno


def desenha(s):
    for i in s:
        desenha(i)


def to_str(s):
    s1 = s[0] + s[1] + s[2]
    return ''.join([to_str(v) for v in s1])
