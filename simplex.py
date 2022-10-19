import numpy as np
from scipy.optimize import linprog
import csv

funcao_objetivo = []
A_ub = []
capacidade = []
A_eq = []
demanda = []
with open('data.csv',  encoding='utf-8') as arquivo:
    tabela = csv.reader(arquivo, delimiter=',')

    next(tabela)  # pula cabeçholho "Distância"
    next(tabela)  # pula cabeçhalho "Capitais"

    tabela = [[linha[0], [int(i) for i in linha[1:]]]
              for i, linha in enumerate(tabela) if linha and i < 5]

    nro_linhas = len(tabela)
    nro_colunas = len(tabela[0][1])

    #Preenchendo a função objetivo, a matriz de restrição de capacidade e a matriz de restrição de demanda
    funcao_objetivo = np.array([])
    
    for i, linha in enumerate(tabela):
        if i < nro_linhas-1:
            funcao_objetivo = np.append(
                funcao_objetivo, linha[1][:nro_colunas-1])
            capacidade = np.append(capacidade, linha[1][nro_colunas-1])
        else:
            demanda = np.append(demanda, linha[1][:nro_colunas-1])

    funcao_objetivo = funcao_objetivo.ravel()
    nro_colunas_func_objetivo = len(funcao_objetivo)

    # Preencher a A_ub
    A_ub = np.zeros((nro_linhas, nro_colunas_func_objetivo))

    start = 0
    end = nro_colunas
    for polo in A_ub:
        polo[start:end] = 1
        start += nro_colunas
        end += nro_colunas

    # Preencher a A_eq
    A_eq = np.zeros((nro_colunas, nro_colunas_func_objetivo))


    print(funcao_objetivo)
    print(A_ub)
    print(demanda)
    print(capacidade)

""" c = [4928, 2444, 5772, 5076]

A_ub = [
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

B_ub = [
    [2876],
    [5385]
]

A_eq = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
]

B_eq = [
    [4243],
    [4002],
]

res = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq,
              b_eq=B_eq, bounds=(0, None), method='simplex')
print(res) """
