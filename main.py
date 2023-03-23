from heuristica import heuristica
from util import filhos

if __name__ == '__main__':
    # start = [[3, 4, 6], [5, 8, 0], [2, 1, 7]]
    # start = [[3, 4, 0], [5, 8, 6], [2, 1, 7]]
    start = [[3, 4, 6], [5, 8, 0], [2, 1, 7]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sucessores = filhos(start)

    print("Terceiro nivel da arvore de busca:")
    for filho in sucessores:
        print(filho)

    valores = []
    for filho in sucessores:
        valor = heuristica(filho, goal)
        valores.append(valor)

    print("Valores correspondentes da função de avaliação para cada nó gerado no Terceiro nível:")
    for i, filho in enumerate(sucessores):
        print(f"{filho}: {valores[i]}")
