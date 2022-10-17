# Fertilizer Optimization

```DESCRIÇÃO```

Integrantes
```

Ryan Souza Sá Teles - 12822062

```

## Modelagem do problema
$x_j$: Quantidade do transportado da origem $i$ ao destino $j$

$c_{ij}$: Custo por unidade do transporte da origem $i$ ao destino $j$

$a_i$ Capacidade de produção da origem $i$

$b$: Demanda do destino

$min$ $\sum\limits_{i=1}^{m} \sum\limits_{j=1}^{n} c_{ij} x_{ij}$

$s.a:$  
$\sum\limits_{j=1}^{n} x_{ij} \leq a$ $\forall i \in \{1,...,m\}$

$\sum\limits_{i=1}^{m} x_{ij} = b_j$ $\forall j \in \{1,...,n\}$

$x_{ij} \geq 0$ $\forall i \in \{1,...,m\}$ $\forall j \in \{1,...,n\}$

## Variávias e Restrições

|              |  AC   |  AL   |  AP   |  AM   |  BA   |  CE   |  DF   |  ES   |  GO   |  MA   |  MT   |  MS   |  MG   |  PA   |  PB   |  PR   |  PE   |  PI   |  RJ   |  RN   |  RS   |  RO   |  RR   |  SC   |  SP   |  SE   |  TO   | Capacidade |
| :----------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--------: |
| Ponta Grossa |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |            |
| Paulínia     |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |            |
| Cubatão      |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |            |
| Rio Grande   |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |       |            |

## Como rodar o projeto
1. Baixe e instale [python](https://www.python.org/) em sua máquina
2. Instale as dependências: `pip install -r requirements.txt`
3. Rode o `main.py` e seja feliz

## Como testar o programa para outras variáveis
https://www.canalrural.com.br/noticias/agricultura/conheca-os-50-municipios-mais-ricos-na-agricultura-brasileira/
