---
layout: default
title: Fertilizer Optimization
---

# Fertilizer Optimization

## **Descrição do problema**
O atual consumo brasileiro de fertilizantes é próximo a 45 milhões de toneladas por ano, o que nos torna o quarto maior consumidor, tendo à nossa frente apenas os Estados Unidos, a Índia e a China. A grande diferença entre o Brasil e os demais grandes consumidores, é que, aqui, 85% do consumo são importados, e esses outros países produzem a maior parte do que consomem. Entre os principais nutrientes necessários para a agricultura estão o nitrogênio, fósforo e potássio, elementos estes que são encontrados em produtos fertilizantes.

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

## **Modelagem do problema**

$$x_j$$: Quantidade do transportado da origem $$i$$ ao destino $$j$$

$$c_{ij}$$: Custo por unidade do transporte da origem $$i$$ ao destino $$j$$

$$a_i$$ Capacidade de produção da origem $$i$$

$$b_i$$: Demanda do destino $$i$$

$$min$$ $$\sum\limits_{i=1}^{m} \sum\limits_{j=1}^{n} c_{ij} x_{ij}$$

$$s.a:$$
$$\sum\limits_{j=1}^{n} x_{ij} \leq a$$ $$\forall i \in \{1,...,m\}$$

$$\sum\limits_{i=1}^{m} x_{ij} = b_j$$ $$\forall j \in \{1,...,n\}$$

$$x_{ij} \geq 0$$ $$\forall i \in \{1,...,m\}$$ $$\forall j \in \{1,...,n\}$$

## **Variávias e Restrições**

### **Tabela de Distâncias**

|Unidades de Produção|Maceió|Natal |Salvador|Vitória|Goiânia|São Luís|Cuiabá|Campo Grande|Belo Horizonte|Belém  |João Pessoa|Curitiba|Recife |Teresina|Porto Alegre|Porto Velho|Florianópolis|São Paulo|Aracaju|Palmas |
|--------------------|------|------|--------|-------|-------|--------|------|------------|--------------|-------|-----------|--------|-------|--------|------------|-----------|-------------|---------|-------|-------|
|Ponta Grossa        |2830  |3343  |2382    |1455   |3120   |3099    |1559  |864         |1089          |3098   |3172       |117     |3059   |2920    |856         |3017       |420          |516      |2576   |1937   |
|Paulínia            |2429  |2942  |1980    |1021   |791    |2773    |1422  |912         |611           |2772   |2771       |504     |2657   |2543    |1232        |2882       |796          |123      |2174   |1612   |
|Cubatão             |2462  |2975  |2014    |991    |966    |2953    |1598  |1043        |644           |2948   |2804       |400     |2690   |2718    |1128        |3058       |692          |59       |2208   |1879   |
|Campo Grande        |2822  |3446  |2485    |1926   |839    |2852    |729   |1           |1269          |2850   |3275       |977     |3162   |2719    |1443        |2189       |2182         |987      |2679   |1690   |

---

### **Tabela Completa**

|Unidades de Produção          |Maceió|Natal |Salvador|Vitória|Goiânia|São Luís|Cuiabá|Campo Grande|Belo Horizonte|Belém  |João Pessoa|Curitiba|Recife |Teresina|Porto Alegre|Porto Velho|Florianópolis|São Paulo|Aracaju|Palmas |**Capacidade**|
|------------------------------|------|------|--------|-------|-------|--------|------|------------|--------------|-------|-----------|--------|-------|--------|------------|-----------|-------------|---------|-------|-------|----------|
|Ponta Grossa                  |11320 |13372 |9528    |5820   |12480  |12396   |6236  |3456        |4356          |12392  |12688      |468     |12236  |11680   |3424        |12068      |1680         |2064     |10304  |7748   |1713280   |
|Paulínia                      |9716  |11768 |7920    |4084   |3164   |11092   |5688  |3648        |2444          |11088  |11084      |2016    |10628  |10172   |4928        |11528      |3184         |492      |8696   |6448   |2141600   |
|Cubatão                       |9848  |11900 |8056    |3964   |3864   |11812   |6392  |4172        |2576          |11792  |11216      |1600    |10760  |10872   |4512        |12232      |2768         |236      |8832   |7516   |1284960   |
|Campo Grande                  |11288 |13784 |9940    |7704   |3356   |11408   |2916  |4           |5076          |11400  |13100      |3908    |12648  |10876   |5772        |8756       |8728         |3948     |10716  |6760   |3854879   |
|**Demandas**                      |36941 |10427 |458371  |108199 |793001 |162918  |1697134|442018      |1000545       |115203 |15694      |1025600 |36900  |107832  |1060803     |32591      |211497       |1068091  |28054  |154583 |          |
|                              |      |      |        |       |       |        |      |            |              |       |           |        |       |        |            |           |             |         |       |       |          |
|**Demanda Total**|*8566399*| |**Capacidade Total**| *8994719*|


---

## **Método Simplex**

O método simplex é desenvolvido na seguinte forma padrão:

$$
Minimizar f(x) = c^Tx \\
            Ax = b\\
            x \geq 0
$$


---

## **Como rodar o projeto**
1. Baixe e instale [python](https://www.python.org/) em sua máquina
2. Instale as dependências: 
   - `pip install BeautifulSoup`
   - `pip install tabulate`
   - `pip install requests`
   - `pip install bs4`
3. Rode  `python main.py` e seja feliz

---

## **Justificativa da extração dos dados**
Todas informações empregadas durante o desenvolvimento do trabalho são verdadeiras, cujas fontes estão disponíveis na seção de bibliografia. Vale frisar a extração/cálculo de três conjuntos de dados em específico:

> **Demandas**: As demandas de fertilizantes de cada estado brasileiro no ano de 2017 em sua origem está representada em milhões de toneladas. Entretanto, há de se considerar que é inatingível que apenas uma empresa seja resposável pela distribuição de toda a demanda do estado, visto que há empresas concorretes. Pensando nisto, foi feito um cálculo base, tomando como apoio que a companhia Yara é responsável por 25% da distruibuição de tais consumos, obtendo os dados finais expostos na tabela. Vale evidenciar que em nosso cenário não há variações de distribuições para cada estado brasileiro, isto é, a empresa é responsável por 25% de toda a demanda do estado (independente do estado).

> **Custos e despesas do transporte**: Para verificar-se a estimativa do custo de entrega dos fertilizantes para cada estado do brasil foi levado em consideração as distâncias entre uma unidade de produção e as respectivas capitais de cada estado, cálculo este que foi feito utilizando a ferramenta do Google Maps. Além disso, foi estimado um custo fixo de R$4,00 por quilômetro rodado de um caminhão, custo este que representa as despesas fixas de um caminhão (impostos), despesas variáveis (manutenção preventiva), despesa por km rodado (levando em consideração o valor do combustível e o total de km rodados no mês). Na semântica do nosso problema não faz diferença um caminhão transportar sua capacidade mínima ou transportar fertilizantes de tal forma que ocupe sua capacidade máxima, em nosso contexto este custo é o mesmo. Ademais, o custo de regresso do veículo à unidade de produção não é relevante para o problema e, portanto, não é considerado.

> **Capacidades de produção de cada unidade**: O único conjunto de dados que não fora encontrado durante a pesquisa foram as capacidades de produção de fertilizantes de cada unidade de produção brasileira da companhia. Logo, a tomada de decisão para definição de tal coleção levou em consideração o tamanho das fábricas, ou seja, fábricas (unidades de produção) maiores, possuem uma maior capacidade de produção. Ademais, as demandas do mercado também foi um modo de medir a distribuição das capacidades de produção das unidades, com o objetivo de atender às necessidades do nicho em questão. 

---

### **Bibliografia**
https://www.npct.com.br/npctweb/npct.nsf/article/BRS-3132

https://www.gov.br/agricultura/pt-br/assuntos/insumos-agropecuarios/insumos-agricolas/fertilizantes/plano-nacional-de-fertilizantes/estatisticas-do-setor#:~:text=O%20principal%20nutriente%20aplicado%20no,no%20Pa%C3%ADs%20(Figura%206).

http://sohelices.com.br/21-maiores-fabricas-de-fertilizantes-do-brasil/#:~:text=As%20quatro%20maiores%20f%C3%A1bricas%20de,segundo%20lugar%20com%20quase%2020%25.

https://blogwlmscania.itaipumg.com.br/como-calcular-o-custo-do-km-rodado-de-um-caminhao-passo-a-passo/

https://www.canalrural.com.br/noticias/agricultura/conheca-os-50-municipios-mais-ricos-na-agricultura-brasileira/

---

## **SME0510 - Introdução à Pesquisa Operacional**
### Integrantes do grupo

```
João Lucas Pereira e Sousa - 10994311
Joel Felipe Coelho - 4865826
Moniely Silva Barboza - 12563800
Ryan Souza Sá Teles - 12822062
```
