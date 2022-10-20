---
layout: default
title: Fertilizer Optimization
---
# Fertilizer Optimization

## **SME0510 - Introdução à Pesquisa Operacional**

### **Integrantes do grupo**

```text
Joel Felipe Coelho            - 4865826
João Lucas Pereira e Sousa    - 10994311
Moniely Silva Barboza         - 12563800
Ryan Souza Sá Teles           - 12822062  
```

---  

## **Descrição do problema**

O atual consumo brasileiro de fertilizantes é próximo a 45 milhões de toneladas por ano, o que nos torna o quarto maior consumidor, tendo à nossa frente apenas os Estados Unidos, a Índia e a China. A grande diferença entre o Brasil e os demais grandes consumidores é que aqui 85% do consumo são importados, enquanto os outros países produzem a maior parte do que consomem. Entre os principais nutrientes necessários para a agricultura estão o nitrogênio, fósforo e potássio, elementos estes que são encontrados em produtos fertilizantes.

Entre as grandes empresas produtoras de fertilizantes, está a Yara, uma companhia que tem ganho notoriedade cada vez mais na maioria dos estados brasileiros. Fundada em 1905 para resolver a fome emergente na Europa, a empresa Yara tem uma presença mundial, tendo 24 unidades misturadoras de fertilizantes, na qual 4 estão localizadas no Brasil.

O Brasil desempenha um papel altamente estratégico nos negócios da Yara, sendo responsável por um terço do volume e um quarto do faturamento global da empresa. Isso significa interagir com mais de 25 mil produtores rurais. Nesse contexto, a companhia investe em soluções competitivas e sustentáveis para todos os tipos de culturas e solos encontrados aqui.

Com a finalidade de tornar possível encontrar a melhor logística de entregas de fertilizantes no Brasil, pretende-se minimizar o custo de entrega dos produtos em todos os estados brasileiros de tal forma que seja rentável para a empresa e satisfaça a demanda dos agricultores. As unidades de produção nacionais da empresa estão localizadas em:

- Ponta Grossa (Estado do Paraná);
- Paulínia (Estado de São Paulo);
- Cubatão (Estado de São Paulo);
- Rio Grande (Estado do Rio Grande do Sul);

Além disto, a corporação apresenta clientes em todas as capitais dos estados brasileiros, com suas respectivas demandas. Estas, por sua vez, representam as requisições de fertilizantes de uma determinada região (expressa em toneladas) que a companhia Yara teve no ano de 2017. Vale ressaltar que as demandas agrículas variam de estado para estado e os estados que possuem mais representatividade de produções agrícolas são: Mato Grosso, São Paulo, Minas Gerais, Rio Grande do Sul e Paraná.

Conjuntamente, é necessário calcular o custo de entrega dos fertilizantes para cada estado do Brasil (considerando que a entrega saía de uma das unidades de produção nacionais), dado que as mesmas são realizadas por via terrestre através de caminhões e carretas. Este custo considera a distância entre uma unidade e a capital do estado em questão, somado à custos operacionais (combustível e manutenção de veículos).

`Por exemplo: Uma entrega de fertilizantes da unidade de produção de Paulínia (localizada no estado de São Paulo) para a capital do estado do Mato Grosso (Cuiabá) dista 1422 quilômetros. O custo operacional total por unidade do transporte de Paulínia à Cuiabá é R$5688 (1422 quilômetros * 4 reais/km).`

Um restringimento da distribuição dessas mercadorias é justamente a capacidade de produção de cada unidade da companhia, a qual mede a capacidade máxima de fertilizantes produzidos (em toneladas) em um período. Tal restrição é de suma importância e faz parte da semântica do problema, sendo necessário ser atendida na elaboração da solução.

---

### **Tabela de Distâncias**

> Tabela Parte 1

| Unidades de Produção | Maceió | Natal | Salvador | Vitória | Goiânia | São Luís | Cuiabá | Campo Grande | Belo Horizonte | Belém |
| :------------------: | :----: | :---: | :------: | :-----: | :-----: | :------: | :----: | :----------: | :------------: | :---: |
|     Ponta Grossa     |  2830  | 3343  |   2382   |  1455   |  3120   |   3099   |  1559  |     864      |      1089      | 3098  |
|       Paulínia       |  2429  | 2942  |   1980   |  1021   |   791   |   2773   |  1422  |     912      |      611       | 2772  |
|       Cubatão        |  2462  | 2975  |   2014   |   991   |   966   |   2953   |  1598  |     1043     |      644       | 2948  |
|     Campo Grande     |  2822  | 3446  |   2485   |  1926   |   839   |   2852   |  729   |      1       |      1269      | 2850  |

> Tabela Parte 2

| Unidades de Produção | João Pessoa | Curitiba | Recife | Teresina | Porto Alegre | Porto Velho | Florianópolis | São Paulo | Aracaju | Palmas |
| :------------------: | :---------: | :------: | :----: | :------: | :----------: | :---------: | :-----------: | :-------: | :-----: | :----: |
|     Ponta Grossa     |    3172     |   117    |  3059  |   2920   |     856      |    3017     |      420      |    516    |  2576   |  1937  |
|       Paulínia       |    2771     |   504    |  2657  |   2543   |     1232     |    2882     |      796      |    123    |  2174   |  1612  |
|       Cubatão        |    2804     |   400    |  2690  |   2718   |     1128     |    3058     |      692      |    59     |  2208   |  1879  |
|     Campo Grande     |    3275     |   977    |  3162  |   2719   |     1443     |    2189     |     2182      |    987    |  2679   |  1690  |

---

## **Modelagem do problema**

$$x_{ij}$$: Quantidade em toneladas de fertilizantes transportada da origem $$i$$ ao destino $$j$$

$$c_{ij}$$: Custo do transporte de fertilizantes da origem $$i$$ ao destino $$j$$

$$a_i$$: Capacidade de produção da origem $$i$$

$$b_i$$: Demanda do destino $$i$$

$$
min \sum\limits_{i=1}^{m} \sum\limits_{j=1}^{n} c_{ij} x_{ij} \\
$$

$$
\sum\limits_{j=1}^{n} x_{ij} \leq a_i \ \ \forall i \in \{1,...,m\}
$$

$$
\sum\limits_{i=1}^{m} x_{ij} = b_j \ \ \forall j \in \{1,...,n\}
$$

$$
x_{ij} \geq 0 \ \ \  \forall i \in \{1,...,m\} \ \ \forall j \in \{1,...,n\}
$$

---

### **Variáveis e Restrições**

Portanto, precisamos respeitar as capacidades dos unidades de produção e atender a demanda de cada estado. Além disso, a quantidade de fertilizantes transportada deve ser maior ou igual a zero.  

#### **Restrições de capacidades de produção de cada unidade:**

$$
x_{1,1}  +  x_{1,2} + \cdots + x_{1, 20} \le 1713280
$$

$$
x_{2,1} + x_{2,2} + \cdots + x_{2, 20} \le 2141600
$$

$$
x_{3,1} + x_{3,2} + \cdots + x_{3, 20} \le 1284960
$$

$$
x_{4,1} + x_{4,2} + \cdots + x_{4, 20} \le 3854879
$$

#### **Restrições de demandas de cada estado brasileiro:**  

$$
x_{1,1} + x_{2,1} + x_{3,1} + x_{4,1} = 36941
$$

$$
x_{1,2} + x_{2,2} + x_{3,2} + x_{4,2} = 10427
$$

$$
x_{1,3} + x_{2,3} + x_{3,3} + x_{4,3} = 458371
$$

$$
x_{1,4} + x_{2,4} + x_{3,4} + x_{4,4} = 108199
$$

$$
x_{1,5} + x_{2,5} + x_{3,5} + x_{4,5} = 793001
$$

$$
x_{1,6} + x_{2,6} + x_{3,6} + x_{4,6} = 162918
$$

$$
x_{1,7} + x_{2,7} + x_{3,7} + x_{4,7} = 1697134
$$

$$
x_{1,8} + x_{2,8} + x_{3,8} + x_{4,8} = 442018
$$

$$
x_{1,9} + x_{2,9} + x_{3,9} + x_{4,9} = 1000545
$$

$$
x_{1,10} + x_{2,10} + x_{3,10} + x_{4,10} = 115203
$$

$$
x_{1,11} + x_{2,11} + x_{3,11} + x_{4,11} = 15694  
$$

$$
x_{1,12} + x_{2,12} + x_{3,12} + x_{4,12} = 1025600
$$

$$
x_{1,13} + x_{2,13} + x_{3,13} + x_{4,13} = 36900  
$$

$$
x_{1,14} + x_{2,14} + x_{3,14} + x_{4,14} = 107832
$$

$$
x_{1,15} + x_{2,15} + x_{3,15} + x_{4,15} = 1060803
$$

$$
x_{1,16} + x_{2,16} + x_{3,16} + x_{4,16} = 32591  
$$

$$
x_{1,17} + x_{2,17} + x_{3,17} + x_{4,17} = 211497
$$

$$
x_{1,18} + x_{2,18} + x_{3,18} + x_{4,18} = 1068091
$$

$$
x_{1,19} + x_{2,19} + x_{3,19} + x_{4,19} = 28054  
$$

$$
x_{1,20} + x_{2,20} + x_{3,20} + x_{4,20} = 154583
$$

---

### **Tabela Completa**

> Tabela Parte 1

| Unidades de Produção | Maceió | Natal | Salvador | Vitória | Goiânia | São Luís | Cuiabá  | Campo Grande | Belo Horizonte | **Capacidade** |
| :------------------: | :----: | :---: | :------: | :-----: | :-----: | :------: | :-----: | :----------: | :------------: | :------------: |
|     Ponta Grossa     | 11320  | 13372 |   9528   |  5820   |  12480  |  12396   |  6236   |     3456     |      4356      |    1713280     |
|       Paulínia       |  9716  | 11768 |   7920   |  4084   |  3164   |  11092   |  5688   |     3648     |      2444      |    2141600     |
|       Cubatão        |  9848  | 11900 |   8056   |  3964   |  3864   |  11812   |  6392   |     4172     |      2576      |    1284960     |
|     Campo Grande     | 11288  | 13784 |   9940   |  7704   |  3356   |  11408   |  2916   |      4       |      5076      |    3854879     |
|     **Demandas**     | 36941  | 10427 |  458371  | 108199  | 793001  |  162918  | 1697134 |    442018    |    1000545     |                |

> Tabela Parte 2

| Unidades de Produção | Belém  | João Pessoa | Curitiba | Recife | Teresina | Porto Alegre | Porto Velho | Florianópolis | **Capacidade** |
| :------------------: | :----: | :---------: | :------: | :----: | :------: | :----------: | :---------: | :-----------: | :------------: |
|     Ponta Grossa     | 12392  |    12688    |   468    | 12236  |  11680   |     3424     |    12068    |     1680      |    1713280     |
|       Paulínia       | 11088  |    11084    |   2016   | 10628  |  10172   |     4928     |    11528    |     3184      |    2141600     |
|       Cubatão        | 11792  |    11216    |   1600   | 10760  |  10872   |     4512     |    12232    |     2768      |    1284960     |
|     Campo Grande     | 11400  |    13100    |   3908   | 12648  |  10876   |     5772     |    8756     |     8728      |    3854879     |
|     **Demandas**     | 115203 |    15694    | 1025600  | 36900  |  107832  |   1060803    |    32591    |    211497     |                |

> Tabela Parte 3

| Unidades de Produção | São Paulo | Aracaju | Palmas | **Capacidade** |
| :------------------: | :-------: | :-----: | :----: | :------------: |
|     Ponta Grossa     |   2064    |  10304  |  7748  |    1713280     |
|       Paulínia       |    492    |  8696   |  6448  |    2141600     |
|       Cubatão        |    236    |  8832   |  7516  |    1284960     |
|     Campo Grande     |   3948    |  10716  |  6760  |    3854879     |
|     **Demandas**     |  1068091  |  28054  | 154583 |                |

| **Demanda Total** | **Capacidade Total** |
| :---------------: | :------------------: |
|     *8566399*     |      *8994719*       |

---

## **Método Simplex**

O método simplex é desenvolvido na seguinte forma padrão:

$$
Minimizar \ \ f(x) = c^Tx
$$

$$
A_{ub}x \leq b_{ub},
$$

$$
A_{eq}x = b_{eq}
$$

$$
l \leq x \leq u
$$

onde $$x$$ é o vetor de variáveis de decisão, $$c$$ é o vetor de custos, $$A_{ub}$$ é a matriz de restrições de desigualdade, $$b_{ub}$$ é o vetor de restrições de desigualdade, $$A_{eq}$$ é a matriz de restrições de igualdade, $$b_{eq}$$ é o vetor de restrições de igualdade, $$l$$ é o vetor de limites inferiores e $$u$$ é o vetor de limites superiores.

### **O Algoritmo Simplex**

O algoritmo do Simplex, consiste, resumidamente, em encontrar a solução ótima para a função objetivo, minimizando-a ou maximizando-a, obedecendo as condições de restrição definidas na modelagem, sendo um procedimento iterativo com um número finito de procedimentos.
A estrutura do método Simplex é composta pelas seguintes etapas:

- **Etapa 1:** Nesta etapa necessita-se de uma solução básica viável inicial, a qual é, um dos pontos extremos do polígono descrito graficamente. Este método verifica se a presente solução é ótima. Se esta não for é porque um dos demais pontos extremos adjacentes (vértice) fornecem um valor menor para a função objetivo que a atual, quando o problema considerado é de minimização. Ele então faz uma mudança de vértice na direção que mais diminua a função objetivo e verifica se este novo vértice é ótimo. A troca de vértice, faz uma variável não básica crescer (assumir valor positivo) ao mesmo tempo em que zera uma variável básica (para possibilitar a troca) conservando a factibilidade. Para isso, escolhemos uma variável, cujo custo relativo é mais negativo (não é regra geral), para entrar na base, e as trocas de vértices são feitas até que não exista mais nenhum custo relativo negativo. A variável que sairá da base é aquela que ao se anular garante que as demais continuem maiores ou iguais a zero, quando aumentamos o valor da variável que entra na base, respeitando assim o conceito de solução básica factível.

Os possíveis resultados neste passo são que uma SBV é encontrada ou que a região viável está vazia (neste último caso o programa linear é chamado de inviável).

- **Etapa 2:** Caso nesta etapa não haja um vértice adjacente melhor que o vértice atual, então PARE. O vértice atual corresponde à solução ótima. Em caso contrário, vá ao Passo 3. Os possíveis resultados do passo 2 são uma solução básica viável ótima ou uma função objetiva ilimitada.

- **Etapa 3:** Encontrar entre os vértices adjacentes uma direção a qual existe uma solução viável melhor e então ir em direção dela; volte ao Passo 2. Ele então faz uma mudança de vértice na direção que mais diminua a função objetivo e verifica se este novo vértice é ótimo.

Vale ressaltar que o algoritmo sempre termina porque o número de vértices no topo do polígono é finito, além disso, como saltamos entre os vértices sempre na mesma direção (a da função objetivo), esperamos que o número de vértices visitados seja pequeno.

### **SciPy - Simplex**

A partir daqui, para utilizar o método simplex e resolver a problemática desenvolvida, vamos utilizar da biblioteca [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html) do Python, mais especificamente, o método [linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html). SciPy é uma biblioteca Python para matemática, ciência e engenharia. Ela fornece muitas rotinas úteis para otimização, álgebra linear, integração numérica, interpolação, processamento de sinais e muito mais.

O método linprog resolve problemas de programação linear, onde o objetivo é minimizar a função linear objetivo, sujeito a restrições lineares. O método linprog recebe como parâmetros:

- **c**: 1-D array
  - Coeficientes da função objetivo a ser minimizada.
- **A_ub**: 2-D array
  - Matriz de restrições de desigualdade. Cada linha da matriz representa uma restrição e cada coluna representa uma variável.
- **b_ub**: 1-D array
  - Vetor de restrições de desigualdade. Cada elemento representa um limite superior para a restrição correspondente.
  - Em nossa modelagem, este parâmetro representava o vetor de capacidades de produção de fertilizantes de cada unidade.
- **A_eq**: 2-D array
  - Matriz de restrições de igualdade. Cada linha da matriz representa uma restrição e cada coluna representa uma variável.
- **b_eq**: 1-D array
  - Vetor de restrições de igualdade. Cada elemento representa um limite inferior para a restrição correspondente.
  - Em nossa modelagem, este parâmetro representava o vetor de demandas de fertilizantes dos estados brasileiros.

---

## **Resultados da otimização de distribuição de fertilizantes**

A seguir, será exposto o resultado da otimização linear do problema de distribuição de fertilizantes. O algoritmo encontrou uma solução ótima viável para o problema, na qual os dados que serão apresentados representam os valores das variáveis de decisão que minimizam a função objetivo, atendendo às restrições definidas:

> Tabela Parte 1

| Unidades de Produção | Maceió | Natal | Salvador | Vitória | Goiânia | São Luís | Cuiabá  | Campo Grande | Belo Horizonte | Belém  |
| :------------------: | :----: | :---: | :------: | :-----: | :-----: | :------: | :-----: | :----------: | :------------: | :----: |
|     Ponta Grossa     |   0    |   0   |    0     |    0    |    0    |    0     |    0    |      0       |       0        |   0    |
|       Paulínia       | 36941  | 10427 |  458371  | 108199  |    0    |    0     |    0    |      0       |    1000545     |   0    |
|       Cubatão        |   0    |   0   |    0     |    0    |    0    |    0     |    0    |      0       |       0        |   0    |
|     Campo Grande     |   0    |   0   |    0     |    0    | 793001  |  162918  | 1697134 |    442018    |       0        | 115203 |
|     **Demandas**     | 36941  | 10427 |  458371  | 108199  | 793001  |  162918  | 1697134 |    442018    |    1000545     | 115203 |

> Tabela Parte 2

| Unidades de Produção | João Pessoa | Curitiba | Recife | Teresina | Porto Alegre | Porto Velho | Florianópolis | São Paulo | Aracaju | Palmas |
| :------------------: | :---------: | :------: | :----: | :------: | :----------: | :---------: | :-----------: | :-------: | :-----: | :----: |
|     Ponta Grossa     |      0      | 1025600  |   0    |    0     |    476183    |      0      |    211497     |     0     |    0    |   0    |
|       Paulínia       |    15694    |    0     | 36900  |  78718   |      0       |      0      |       0       |  367751   |  28054  |   0    |
|       Cubatão        |      0      |    0     |   0    |    0     |    584620    |      0      |       0       |  700340   |    0    |   0    |
|     Campo Grande     |      0      |    0     |   0    |  29114   |      0       |    32591    |       0       |     0     |    0    | 154583 |
|     **Demandas**     |    15694    | 1025600  | 36900  |  107832  |   1060803    |    32591    |    211497     |  1068091  |  28054  | 154583 |

---

## **Justificativa da extração dos dados**

Todas informações empregadas durante o desenvolvimento do trabalho são verdadeiras, cujas fontes estão disponíveis na seção de bibliografia. Vale frisar a extração/cálculo de três conjuntos de dados em específico:

> **Demandas**: As demandas de fertilizantes de cada estado brasileiro no ano de 2017 em sua origem está representada em milhões de toneladas. Entretanto, há de se considerar que é inatingível que apenas uma empresa seja responsável pela distribuição de toda a demanda do estado, visto que há empresas concorretes. Pensando nisto, foi feito um cálculo base, tomando como apoio que a companhia Yara é responsável por 25% da distruibuição de tais consumos, obtendo os dados finais expostos na tabela. Vale evidenciar que em nosso cenário não há variações de distribuições para cada estado brasileiro, isto é, a empresa é responsável por 25% de toda a demanda do estado (independente do estado).

> **Custos e despesas do transporte**: Para verificar-se a estimativa do custo de entrega dos fertilizantes para cada estado do brasil foi levado em consideração as distâncias entre uma unidade de produção e as respectivas capitais de cada estado, cálculo este que foi feito utilizando a ferramenta do Google Maps. Além disso, foi estimado um custo fixo de R$4,00 por quilômetro rodado de um caminhão, custo este que representa as despesas fixas de um caminhão (impostos), despesas variáveis (manutenção preventiva), despesa por km rodado (levando em consideração o valor do combustível e o total de km rodados no mês). Na semântica do nosso problema não faz diferença um caminhão transportar sua capacidade mínima ou transportar fertilizantes de tal forma que ocupe sua capacidade máxima, em nosso contexto este custo é o mesmo. Ademais, o custo de regresso do veículo à unidade de produção não é relevante para o problema e, portanto, não é considerado.

> **Capacidades de produção de cada unidade**: O único conjunto de dados que não fora encontrado durante a pesquisa foram as capacidades de produção de fertilizantes de cada unidade de produção brasileira da companhia. Logo, a tomada de decisão para definição de tal coleção levou em consideração o tamanho das fábricas, ou seja, fábricas (unidades de produção) maiores, possuem uma maior capacidade de produção. Ademais, as demandas do mercado também foi um modo de medir a distribuição das capacidades de produção das unidades, com o objetivo de atender às necessidades do nicho em questão.

---

## **Como rodar o projeto**

1. Baixe e instale [python](https://www.python.org/) em sua máquina
2. Instale as dependências:
   - `pip install numpy`
   - `pip install scipy`
3. Rode  `python script.py` e seja feliz

---

## **Bibliografia**

<https://www.npct.com.br/npctweb/npct.nsf/article/BRS-3132>

<https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes/plano-nacional-de-fertilizantes/estatisticas-do-setor#:~:text=O%20principal%20nutriente%20aplicado%20no,no%20Pa%C3%ADs%20(Figura%206>).

<http://sohelices.com.br/21-maiores-fabricas-de-fertilizantes-do-brasil/#:~:text=As%20quatro%20maiores%20f%C3%A1bricas%20de,segundo%20lugar%20com%20quase%2020%25>.

<https://blogwlmscania.itaipumg.com.br/como-calcular-o-custo-do-km-rodado-de-um-caminhao-passo-a-passo/>

<https://www.canalrural.com.br/noticias/agricultura/conheca-os-50-municipios-mais-ricos-na-agricultura-brasileira/>

---
