from heapq import heappush, heappop

from util import filhos, to_str


def busca_a_star(start, goal, heuristica):
    h = []
    heappush(h, (heuristica(start, goal), start))
    pais = dict()
    visited = [start]

    while len(h) > 0:
        (_, pai) = heappop(h)
        for filho in filhos(pai):
            if filho not in visited:
                visited.append(filho)
                pais[to_str(filho)] = pai
                no = filho
                res = []
                profund = 0
                while no != start:
                    res.append(no)
                    no = pais[to_str(no)]
                    profund += 1
                res.append(start)
                res.reverse()
                if filho == goal:
                    print(len(visited))
                    return res
                else:
                    heappush(h, (heuristica(filho, goal) + profund, filho))
    print("erro")
