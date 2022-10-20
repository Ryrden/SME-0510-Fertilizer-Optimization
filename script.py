import numpy as np
from scipy.optimize import linprog
import csv

def preenche_c(tabela, nro_cidades):
    return np.array([linha[1][:nro_cidades] for linha in tabela[:nro_polos]]).ravel()

def preenche_A_ub(nro_cidades, nro_cidades_func_objetivo: int):
    A_ub = np.zeros((nro_polos, nro_cidades_func_objetivo))

    comeco = 0
    final = nro_cidades
    for polo in A_ub:
        polo[comeco:final] = 1
        comeco += nro_cidades
        final += nro_cidades

    return A_ub

def preenche_b_ub(tabela, nro_cidades):
    return np.array([linha[1][nro_cidades] for linha in tabela[:nro_polos]])

def preenche_b_eq(tabela, nro_cidades):
    return np.array([linha[1][:nro_cidades] for linha in tabela[nro_polos:]]).ravel()

def preenche_A_eq(nro_cidades, nro_cidades_func_objetivo: int):
    A_eq = np.zeros((nro_cidades, nro_cidades_func_objetivo))
    for i in range(nro_cidades):
        A_eq[i][i] = 1
        if i+nro_cidades < nro_cidades_func_objetivo:
            A_eq[i][i+nro_cidades] = 1
        if i+nro_cidades*2 < nro_cidades_func_objetivo:
            A_eq[i][i+nro_cidades*2] = 1
        if i+nro_cidades*3 < nro_cidades_func_objetivo:
            A_eq[i][i+nro_cidades*3] = 1
    return A_eq


funcao_objetivo = []
A_ub = []
capacidade = []
A_eq = []
demanda = []
with open('data.csv',  encoding='utf-8') as arquivo:
    tabela = csv.reader(arquivo, delimiter=',')

    next(tabela)  # pula cabeçalho "Distância"
    next(tabela)  # pula cabeçalho "Capitais"

    tabela = [[linha[0], [int(j) for j in linha[1:]]]
              for i, linha in enumerate(tabela) if linha and i < 5]

    nro_polos = len(tabela)-1
    nro_cidades = len(tabela[0][1])-1

    funcao_objetivo = preenche_c(tabela, nro_cidades)
    capacidade = preenche_b_ub(tabela, nro_cidades)
    demanda = preenche_b_eq(tabela, nro_cidades)

    nro_cidades_func_objetivo = len(funcao_objetivo)

    A_ub = preenche_A_ub(nro_cidades, nro_cidades_func_objetivo)

    A_eq = preenche_A_eq(nro_cidades, nro_cidades_func_objetivo)

capacidade = [
    [1713280],
    [2141600],
    [1284960],
    [3854879]
]

res = linprog(funcao_objetivo, A_ub=A_ub, b_ub=capacidade,
              A_eq=A_eq, b_eq=demanda, bounds=(0, None), method='simplex')
print(res)

with open('resultado.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Maceió", "Natal", "Salvador", "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém",
                    "João Pessoa", "Curitiba", "Recife", "Teresina", "Porto Alegre", "Porto Velho", "Florianópolis", "São Paulo", "Aracaju", "Palmas"])

    comeco = 0
    final = 20
    for i in range(4):
        writer.writerow(res.x[comeco:final])
        comeco += 20
        final += 20
